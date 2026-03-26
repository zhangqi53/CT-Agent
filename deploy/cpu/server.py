"""
CT-Agent CPU Backend Service
FastAPI server exposing CPU-based medical CT utility tools.
Port: 35678
"""

import logging
import time
import sys
import os
import json
import traceback
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
import uvicorn

LOG_DIR = Path(os.environ.get("LOG_DIR", "/app/logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler(LOG_DIR / f"cpu-{datetime.now():%Y-%m-%d}.log"),
    ],
)
log = logging.getLogger("cpu-main")

BUILD_LOG = LOG_DIR / "build.log"

def build_log(step: str, status: str, detail: str = ""):
    entry = f"[{datetime.now().isoformat()}] [BUILD] [{step}] {status} {detail}"
    log.info(entry)
    with open(BUILD_LOG, "a") as f:
        f.write(entry + "\n")

app = FastAPI(title="CT-Agent CPU Backend", version="0.1.0")

TOOLS: dict[str, dict] = {}
TOOL_LOAD_ERRORS: dict[str, str] = {}

def register_tool(name: str, handler, description: str = ""):
    TOOLS[name] = {"handler": handler, "description": description}
    build_log(name, "REGISTERED", description[:80])

# ============================================================
# TOOL LOADING
# ============================================================

# --- pyradiomics ---
try:
    build_log("pyradiomics", "LOADING")
    from radiomics import featureextractor
    import SimpleITK as sitk

    _extractor = None

    def run_pyradiomics(params: dict) -> dict:
        global _extractor
        if _extractor is None:
            settings = {"binWidth": 25, "resampledPixelSpacing": None}
            _extractor = featureextractor.RadiomicsFeatureExtractor(**settings)
            feature_classes = params.get("feature_classes")
            if feature_classes:
                _extractor.disableAllFeatures()
                for cls in feature_classes:
                    _extractor.enableFeatureClassByName(cls)

        volume_path = params["volume_path"]
        mask_path = params["mask_path"]

        result = _extractor.execute(volume_path, mask_path)
        features = {k: float(v) if hasattr(v, '__float__') else str(v) for k, v in result.items() if not k.startswith("diagnostics_")}
        diagnostics = {k: str(v) for k, v in result.items() if k.startswith("diagnostics_")}

        return {"features": features, "diagnostics": diagnostics, "num_features": len(features)}

    register_tool("pyradiomics", run_pyradiomics, "1500+ radiomics features extraction")
    build_log("pyradiomics", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["pyradiomics"] = traceback.format_exc()
    build_log("pyradiomics", "FAIL", str(e))

# --- SimpleITK utilities ---
try:
    build_log("simpleITK_utils", "LOADING")
    import SimpleITK as sitk
    import numpy as np

    def run_dicom2nifti(params: dict) -> dict:
        dicom_dir = params["dicom_dir"]
        output_path = params.get("output_path", "/tmp/converted.nii.gz")
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
        if not dicom_names:
            raise ValueError(f"No DICOM files found in {dicom_dir}")
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
        sitk.WriteImage(image, output_path)
        size = list(image.GetSize())
        spacing = [round(s, 3) for s in image.GetSpacing()]
        return {"output_path": output_path, "size": size, "spacing": spacing, "num_slices": len(dicom_names)}

    def run_window_level(params: dict) -> dict:
        PRESETS = {
            "lung": (1500, -600), "mediastinum": (400, 40), "bone": (1800, 400),
            "liver": (150, 30), "brain": (80, 40), "soft_tissue": (350, 50),
            "stroke": (40, 40), "subdural": (200, 75),
        }
        volume_path = params["volume_path"]
        img = sitk.ReadImage(volume_path)

        preset = params.get("preset")
        if preset and preset in PRESETS:
            ww, wl = PRESETS[preset]
        else:
            ww = params.get("custom_ww", 400)
            wl = params.get("custom_wl", 40)

        lower = wl - ww / 2
        upper = wl + ww / 2
        windowed = sitk.IntensityWindowing(img, lower, upper, 0, 255)
        output_path = params.get("output_path", volume_path.replace(".nii", f"_wl{wl}_ww{ww}.nii"))
        sitk.WriteImage(windowed, output_path)
        return {"output_path": output_path, "ww": ww, "wl": wl}

    def run_mask_to_bbox(params: dict) -> dict:
        mask_path = params["mask_path"]
        mask = sitk.ReadImage(mask_path)
        stats = sitk.LabelShapeStatisticsImageFilter()
        stats.Execute(mask)
        labels = stats.GetLabels()
        bboxes = {}
        for label in labels:
            bb = stats.GetBoundingBox(label)
            n = len(bb) // 2
            bboxes[int(label)] = {
                "start": list(bb[:n]),
                "size": list(bb[n:]),
                "centroid": [round(c, 2) for c in stats.GetCentroid(label)],
                "volume_mm3": round(stats.GetPhysicalSize(label), 2),
            }
        return {"bboxes": bboxes, "num_labels": len(labels)}

    def run_dicom_metadata(params: dict) -> dict:
        import pydicom
        dicom_path = params["dicom_path"]
        if os.path.isdir(dicom_path):
            files = [f for f in os.listdir(dicom_path) if f.endswith(".dcm") or not f.startswith(".")]
            if files:
                dicom_path = os.path.join(dicom_path, files[0])
        ds = pydicom.dcmread(dicom_path, stop_before_pixels=True)
        tags = params.get("tags", [
            "PatientID", "PatientAge", "PatientSex", "StudyDate", "Modality",
            "SliceThickness", "KVP", "ContrastBolusAgent", "Manufacturer",
            "InstitutionName", "StudyDescription", "SeriesDescription",
        ])
        result = {}
        for tag in tags:
            val = getattr(ds, tag, None)
            result[tag] = str(val) if val is not None else None
        return result

    register_tool("dicom2nifti", run_dicom2nifti, "DICOM→NIfTI conversion with orientation normalization")
    register_tool("window_level", run_window_level, "Window/level transformation (8 presets + custom)")
    register_tool("mask_to_bbox", run_mask_to_bbox, "Segmentation mask → 3D bounding boxes + centroids + volumes")
    register_tool("dicom_metadata", run_dicom_metadata, "Read DICOM metadata tags")
    build_log("simpleITK_utils", "OK", "4 tools")
except Exception as e:
    TOOL_LOAD_ERRORS["simpleITK_utils"] = traceback.format_exc()
    build_log("simpleITK_utils", "FAIL", str(e))

# --- cc3d postprocessing ---
try:
    build_log("cc3d_filter", "LOADING")
    import cc3d
    import nibabel as nib
    import numpy as np

    def run_cc3d_filter(params: dict) -> dict:
        mask_path = params["mask_path"]
        min_volume_ml = params.get("min_volume_ml", 0.5)
        keep_largest_k = params.get("keep_largest_k")

        img = nib.load(mask_path)
        data = np.asarray(img.dataobj).astype(np.uint32)
        voxel_vol = float(np.prod(img.header.get_zooms())) / 1000  # mL

        if keep_largest_k:
            filtered = cc3d.largest_k(data, k=keep_largest_k)
        else:
            min_voxels = int(min_volume_ml / voxel_vol) if voxel_vol > 0 else 10
            filtered = cc3d.dust(data, threshold=min_voxels)

        output_path = params.get("output_path", mask_path.replace(".nii", "_filtered.nii"))
        out_img = nib.Nifti1Image(filtered.astype(np.int16), img.affine, img.header)
        nib.save(out_img, output_path)

        original_count = len(np.unique(data)) - 1
        filtered_count = len(np.unique(filtered)) - 1
        return {"output_path": output_path, "original_components": original_count, "remaining_components": filtered_count}

    register_tool("cc3d_filter", run_cc3d_filter, "Connected component filtering (remove small objects / keep largest K)")
    build_log("cc3d_filter", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["cc3d_filter"] = traceback.format_exc()
    build_log("cc3d_filter", "FAIL", str(e))

# --- RECIST calculator ---
try:
    build_log("recist_calculator", "LOADING")
    import nibabel as nib
    import numpy as np
    from scipy import ndimage

    def run_recist(params: dict) -> dict:
        mask_path = params["mask_path"]
        img = nib.load(mask_path)
        data = np.asarray(img.dataobj)
        spacing = img.header.get_zooms()

        # Find the axial slice with largest cross-section
        label = params.get("label", 1)
        binary = (data == label).astype(np.uint8)
        slice_areas = np.sum(binary, axis=(0, 1))  # sum over x,y for each z
        max_z = int(np.argmax(slice_areas))

        # Get contour points on that slice
        slice_2d = binary[:, :, max_z]
        if np.sum(slice_2d) == 0:
            return {"error": "No voxels found for the specified label"}

        # Find contour
        from skimage.measure import find_contours, regionprops
        props = regionprops(slice_2d.astype(int))
        if not props:
            return {"error": "No regions found"}

        p = props[0]
        # Long axis = major_axis_length * pixel spacing
        long_axis_mm = round(p.major_axis_length * float(spacing[0]), 2)
        short_axis_mm = round(p.minor_axis_length * float(spacing[1]), 2)

        # Volume
        voxel_vol = float(np.prod(spacing)) / 1000
        volume_ml = round(float(np.sum(binary)) * voxel_vol, 2)

        return {
            "long_axis_mm": long_axis_mm,
            "short_axis_mm": short_axis_mm,
            "max_axial_slice": max_z,
            "volume_ml": volume_ml,
            "voxel_count": int(np.sum(binary)),
        }

    register_tool("recist_calculator", run_recist, "RECIST long/short axis diameter + volume from segmentation mask")
    build_log("recist_calculator", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["recist_calculator"] = traceback.format_exc()
    build_log("recist_calculator", "FAIL", str(e))

# --- Volume change / VDT ---
try:
    build_log("volume_change", "LOADING")
    import math

    def run_volume_change(params: dict) -> dict:
        v1 = params["baseline_volume_ml"]
        v2 = params["followup_volume_ml"]
        days = params["interval_days"]

        if v1 <= 0 or v2 <= 0:
            return {"error": "Volumes must be positive"}

        change_pct = round((v2 - v1) / v1 * 100, 2)
        change_abs = round(v2 - v1, 2)

        vdt_days = None
        if v2 != v1 and days > 0:
            vdt_days = round(days * math.log(2) / math.log(v2 / v1), 1)

        # RECIST response
        if change_pct <= -30:
            recist = "PR"
        elif change_pct >= 20:
            recist = "PD"
        elif v2 == 0:
            recist = "CR"
        else:
            recist = "SD"

        return {
            "baseline_ml": v1, "followup_ml": v2,
            "change_pct": change_pct, "change_abs_ml": change_abs,
            "vdt_days": vdt_days, "recist_response": recist,
            "interval_days": days,
        }

    register_tool("volume_change", run_volume_change, "Volume change rate + VDT + RECIST response assessment")
    build_log("volume_change", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["volume_change"] = traceback.format_exc()
    build_log("volume_change", "FAIL", str(e))

# --- FHIR export ---
try:
    build_log("fhir_export", "LOADING")

    def run_fhir_export(params: dict) -> dict:
        from fhir.resources.diagnosticreport import DiagnosticReport
        from fhir.resources.observation import Observation
        from datetime import datetime

        findings = params["findings"]
        patient_id = params.get("patient_id", "anonymous")
        study_uid = params.get("study_uid", "unknown")

        report = DiagnosticReport(
            status="final",
            code={"coding": [{"system": "http://loinc.org", "code": "18748-4", "display": "Diagnostic imaging study"}]},
            subject={"reference": f"Patient/{patient_id}"},
            effectiveDateTime=datetime.now().isoformat(),
            conclusion=findings.get("conclusion", "See detailed findings"),
        )
        return {"fhir_resource": json.loads(report.model_dump_json()), "resource_type": "DiagnosticReport"}

    register_tool("fhir_export", run_fhir_export, "Export findings as HL7 FHIR R4 DiagnosticReport")
    build_log("fhir_export", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["fhir_export"] = traceback.format_exc()
    build_log("fhir_export", "FAIL", str(e))

# --- NLP tools (medspaCy, NegBio) ---
try:
    build_log("medspacy_negation", "LOADING")
    import medspacy

    _nlp = None

    def run_negation(params: dict) -> dict:
        global _nlp
        if _nlp is None:
            _nlp = medspacy.load()

        text = params["text"]
        doc = _nlp(text)
        entities = []
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
                "is_negated": ent._.is_negated,
                "is_uncertain": ent._.is_uncertain if hasattr(ent._, "is_uncertain") else None,
            })
        return {"entities": entities, "num_entities": len(entities)}

    register_tool("medspacy_negation", run_negation, "Clinical NER + negation/uncertainty detection (ConText)")
    build_log("medspacy_negation", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["medspacy_negation"] = traceback.format_exc()
    build_log("medspacy_negation", "FAIL", str(e))

# --- Placeholder for remaining CPU tools ---
PLACEHOLDER_CPU_TOOLS = [
    ("antspy_register", "Image registration (rigid/affine/SyN)"),
    ("vmtk_vascular", "Vascular analysis (centerline/cross-section)"),
    ("worc_radiomics", "Automated radiomics classification pipeline"),
    ("highdicom_sr", "DICOM Structured Report creation (TID1500)"),
    ("radgraph_ner", "Report NER + relation extraction"),
    ("chexbert_labels", "Report 14-class label classification"),
    ("sarle_labeler", "83 abnormalities × 52 body regions text labeling"),
    ("famesumm", "Multi-organ report summarization"),
    ("multi_label_body_ct", "3-system multi-label CT report classification"),
    ("radiomics_liver_fibrosis", "Liver fibrosis CT grading"),
    ("body_region_classifier", "CT body part identification"),
    ("body_organ_analysis", "Full body organ + composition analysis"),
    ("comp2comp", "Body composition + bone density + aortic calcium"),
    ("deepcac", "Coronary artery calcium quantification"),
    ("ai_cac", "Non-gated calcium scoring"),
    ("segment_cacs", "Segment-level coronary calcium scoring"),
    ("ramac_fda", "Longitudinal lesion matching (FDA classical algorithm)"),
]

for name, desc in PLACEHOLDER_CPU_TOOLS:
    def make_ph(n, d):
        def handler(params: dict) -> dict:
            return {"status": "not_implemented", "tool": n}
        register_tool(n, handler, f"[PLACEHOLDER] {d}")
    make_ph(name, desc)

build_log("ALL_TOOLS", "DONE", f"Loaded {len(TOOLS)} tools ({len(TOOL_LOAD_ERRORS)} errors)")

# ============================================================
# API ENDPOINTS (same structure as GPU backend)
# ============================================================

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "tools_loaded": len(TOOLS),
        "tools_failed": len(TOOL_LOAD_ERRORS),
        "failed_list": list(TOOL_LOAD_ERRORS.keys()),
        "timestamp": datetime.now().isoformat(),
    }

@app.get("/tools")
async def list_tools():
    return {name: {"description": info["description"]} for name, info in TOOLS.items()}

@app.get("/build-log")
async def get_build_log():
    if BUILD_LOG.exists():
        return {"log": BUILD_LOG.read_text()}
    return {"log": "No build log found"}

@app.get("/errors")
async def get_errors():
    return TOOL_LOAD_ERRORS

@app.post("/tools/{tool_name}")
async def call_tool(tool_name: str, request: Request):
    if tool_name not in TOOLS:
        raise HTTPException(404, f"Tool '{tool_name}' not found")
    params = await request.json()
    start = time.time()
    log.info(f"[{tool_name}] Called with params: {list(params.keys())}")
    try:
        result = TOOLS[tool_name]["handler"](params)
        elapsed = time.time() - start
        log.info(f"[{tool_name}] OK in {elapsed:.2f}s")
        return {"result": result, "elapsed_seconds": round(elapsed, 2)}
    except Exception as e:
        elapsed = time.time() - start
        tb = traceback.format_exc()
        log.error(f"[{tool_name}] FAIL in {elapsed:.2f}s: {e}")
        raise HTTPException(500, detail={"error": str(e), "traceback": tb[:1000]})

@app.on_event("startup")
async def startup():
    build_log("SERVER", "START", f"CPU backend on port {os.environ.get('PORT', 35678)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 35678))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
