"""
CT-Agent GPU Backend Service
FastAPI server exposing GPU-based medical CT tools.
Port: 35677
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
from fastapi.responses import JSONResponse
import uvicorn

# --- Logging ---
LOG_DIR = Path(os.environ.get("LOG_DIR", "/app/logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stderr),
        logging.FileHandler(LOG_DIR / f"gpu-{datetime.now():%Y-%m-%d}.log"),
    ],
)
log = logging.getLogger("gpu-main")

# --- Build log ---
BUILD_LOG = LOG_DIR / "build.log"

def build_log(step: str, status: str, detail: str = ""):
    entry = f"[{datetime.now().isoformat()}] [BUILD] [{step}] {status} {detail}"
    log.info(entry)
    with open(BUILD_LOG, "a") as f:
        f.write(entry + "\n")

# --- App ---
app = FastAPI(title="CT-Agent GPU Backend", version="0.1.0")

# --- Tool registry ---
TOOLS: dict[str, dict] = {}
TOOL_LOAD_ERRORS: dict[str, str] = {}

def register_tool(name: str, handler, description: str = ""):
    TOOLS[name] = {"handler": handler, "description": description}
    build_log(name, "REGISTERED", description[:80])

# ============================================================
# TOOL LOADING — each tool in a try/except so one failure
# doesn't take down the whole server
# ============================================================

# --- TotalSegmentator ---
try:
    build_log("totalsegmentator", "LOADING")
    from totalsegmentator.python_api import totalsegmentator
    import nibabel as nib
    import numpy as np

    def run_totalsegmentator(params: dict) -> dict:
        input_path = params["volume_path"]
        task = params.get("task", "total")
        fast = params.get("fast", False)
        output_path = params.get("output_path", input_path.replace(".nii", "_seg.nii"))

        img = nib.load(input_path)
        output_img = totalsegmentator(img, task=task, fast=fast)
        nib.save(output_img, output_path)

        # Basic stats
        data = np.asarray(output_img.dataobj)
        labels = np.unique(data[data > 0])
        voxel_vol = float(np.prod(output_img.header.get_zooms())) / 1000  # mL

        stats = {}
        for label_id in labels:
            vol = float(np.sum(data == label_id)) * voxel_vol
            stats[int(label_id)] = {"volume_ml": round(vol, 2)}

        return {"output_path": output_path, "num_labels": len(labels), "stats": stats}

    register_tool("totalsegmentator", run_totalsegmentator, "117-class anatomy segmentation")
    build_log("totalsegmentator", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["totalsegmentator"] = traceback.format_exc()
    build_log("totalsegmentator", "FAIL", str(e))

# --- lungmask ---
try:
    build_log("lungmask", "LOADING")
    from lungmask import LMInferer
    import SimpleITK as sitk

    _lungmask_inferer = None

    def run_lungmask(params: dict) -> dict:
        global _lungmask_inferer
        if _lungmask_inferer is None:
            model = params.get("model", "LTRCLobes")
            _lungmask_inferer = LMInferer(modelname=model)

        input_path = params["volume_path"]
        img = sitk.ReadImage(input_path)
        seg = _lungmask_inferer.apply(img)

        output_path = params.get("output_path", input_path.replace(".nii", "_lung.nii"))
        out_img = sitk.GetImageFromArray(seg)
        out_img.CopyInformation(img)
        sitk.WriteImage(out_img, output_path)

        labels = {int(v) for v in seg.flat if v > 0}
        return {"output_path": output_path, "lobe_labels": sorted(labels)}

    register_tool("lungmask", run_lungmask, "Lung/lobe segmentation (R231/LTRCLobes)")
    build_log("lungmask", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["lungmask"] = traceback.format_exc()
    build_log("lungmask", "FAIL", str(e))

# --- BLAST-CT ---
try:
    build_log("blast_ct", "LOADING")
    # blast-ct is a CLI tool, wrap it
    import subprocess

    def run_blast_ct(params: dict) -> dict:
        input_path = params["volume_path"]
        output_dir = params.get("output_dir", "/tmp/blast_ct_output")
        os.makedirs(output_dir, exist_ok=True)

        result = subprocess.run(
            ["blast-ct", "--input", input_path, "--output", output_dir],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            raise RuntimeError(f"blast-ct failed: {result.stderr[:500]}")

        # Parse output files
        outputs = list(Path(output_dir).glob("*.nii*"))
        return {"output_dir": output_dir, "files": [str(f) for f in outputs], "stdout": result.stdout[:500]}

    register_tool("blast_ct", run_blast_ct, "TBI lesion detection+segmentation (Lancet Digital Health 2020)")
    build_log("blast_ct", "OK")
except Exception as e:
    TOOL_LOAD_ERRORS["blast_ct"] = traceback.format_exc()
    build_log("blast_ct", "FAIL", str(e))

# --- Generic placeholder for tools not yet implemented ---
def make_placeholder(tool_name: str, description: str):
    def handler(params: dict) -> dict:
        return {"status": "not_implemented", "tool": tool_name, "message": f"{tool_name} is registered but not yet implemented"}
    register_tool(tool_name, handler, f"[PLACEHOLDER] {description}")

# Register remaining tools as placeholders (to be implemented)
PLACEHOLDER_TOOLS = [
    ("cads_segmentation", "167-class anatomy segmentation"),
    ("vista3d", "127-class foundation segmentation model"),
    ("medsam", "Interactive prompt-based 3D segmentation"),
    ("sam_med3d", "3D prompt segmentation with minimal clicks"),
    ("medsam2", "3D segmentation + CT lesion checkpoint"),
    ("mullet", "Multi-phase liver lesion segmentation"),
    ("totalspineseg", "Vertebra/disc/cord segmentation"),
    ("skellytour", "Bone segmentation 17/38/60 labels"),
    ("ovseg", "Ovarian cancer CT segmentation"),
    ("livermask", "Liver parenchyma segmentation"),
    ("fracsegnet", "Pelvic fracture segmentation"),
    ("ctpelvic1k", "Pelvic bone segmentation"),
    ("usam_care", "Rectal cancer CT segmentation"),
    ("hilab_hn_gtv", "Nasopharyngeal carcinoma GTV segmentation"),
    ("parotid_seg", "Parotid gland CT segmentation"),
    ("monai_lung_nodule_detection", "3D RetinaNet lung nodule detection"),
    ("monai_spleen_seg", "Spleen CT segmentation"),
    ("monai_pancreas_seg", "Pancreas + tumor segmentation"),
    ("monai_btcv_seg", "13 abdominal organ segmentation"),
    ("monai_multi_organ_seg", "7 abdominal organ segmentation"),
    ("monai_renal_cect_seg", "Renal structures segmentation"),
    ("monai_renal_unest_seg", "Renal cortex/medulla segmentation"),
    ("monai_wholebody_seg", "104-class whole-body segmentation"),
    ("monai_pediatric_seg", "Pediatric abdominal segmentation"),
    ("rsna_ich", "ICH 5-subtype classification (AUC 0.988)"),
    ("deepbleed", "ICH segmentation + volume quantification"),
    ("penet", "Pulmonary embolism detection (AUROC 0.85)"),
    ("pandx", "Pancreatic cancer detection (PANORAMA 1st)"),
    ("cect_pdac_detection", "PDAC automatic detection (10 models)"),
    ("ai_lung_health", "Lung nodule malignancy classification"),
    ("lung_nodule_clf", "Lung nodule segmentation + classification"),
    ("kidney_tumor_clf", "Kidney tumor detection + classification"),
    ("ct_colonography_polyp", "CTC polyp benign/malignant classification"),
    ("maskrcnn_ribfrac", "Rib fracture detection (>97% acc)"),
    ("vcfnet", "Vertebral compression fracture classification"),
    ("sato_anomaly", "Multi-organ anomaly detection (7 organs)"),
    ("dl_bone_lesion", "Bone metastasis detection + classification"),
    ("pleural_effusion", "Pleural effusion detection + classification"),
    ("ascites_model", "Ascites detection + volume quantification"),
    ("liver_lesion_detection", "Liver lesion detection"),
    ("ct_mediastinal_structures", "Mediastinal lymph node segmentation"),
    ("lesionlocator", "Whole-body tumor longitudinal tracking"),
    ("unigradicon", "CT deformable registration foundation model"),
    ("detect_then_track", "RECIST longitudinal evaluation"),
    ("longiseg", "Longitudinal segmentation with temporal weighting"),
    ("strokevit", "ASPECTS stroke scoring"),
    ("acute_stroke_pipeline", "Stroke detection + segmentation"),
    ("nodulenet", "Lung nodule detection + segmentation"),
    ("gtrnet", "Gastric cancer T-staging (AUC 0.86-0.95)"),
    ("rsna_trauma", "Spleen/liver/kidney injury grading"),
    ("flare22", "Abdominal 13-organ segmentation (challenge winner)"),
    ("hecktor", "Head-neck tumor PET/CT segmentation"),
    ("autopet3", "Whole-body tumor PET/CT segmentation"),
    ("sega", "Aorta segmentation (Dice 0.920)"),
    ("stoic", "COVID severity prediction"),
    ("abdomenct1k", "Liver/kidney/spleen/pancreas segmentation"),
    ("parse2022", "Pulmonary artery segmentation"),
    ("luna16", "Lung nodule detection"),
    ("ct_fm", "CT self-supervised foundation model (148K CTs)"),
    ("suprem", "Pretrained backbone (ICLR 2024 Oral)"),
    ("stu_net", "1.4B parameter CT segmentation model"),
    ("ct_sam3d", "107-class interactive 3D segmentation"),
    ("models_genesis", "Classic CT self-supervised pretraining"),
    ("pumit", "Universal medical image transformer"),
    ("ct_clip", "Zero-shot 18-pathology CT classification"),
    ("ct_chat", "CT VQA + report generation (chest)"),
    ("m3d_lamed", "3D medical VLM multi-task"),
    ("med3dvlm", "3D CT VLM (outperforms M3D)"),
    ("forte_braingpt", "Brain CT report generation (F1=0.71)"),
    ("radgpt", "Abdominal CT tumor report generation"),
    ("ct_graph", "Anatomy-guided CT report generation"),
    ("universeg", "Few-shot segmentation (no retraining)"),
    ("mi_prediction", "Coronary stenosis prediction"),
    ("pansegnet", "Pancreas segmentation (CT+MRI)"),
    ("pact3d", "Pneumoperitoneum detection"),
]

for name, desc in PLACEHOLDER_TOOLS:
    make_placeholder(name, desc)

build_log("ALL_TOOLS", "DONE", f"Loaded {len(TOOLS)} tools ({len(TOOL_LOAD_ERRORS)} errors)")

# ============================================================
# API ENDPOINTS
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
    return {
        name: {"description": info["description"], "status": "active"}
        for name, info in TOOLS.items()
    }

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
        raise HTTPException(404, f"Tool '{tool_name}' not found. Available: {list(TOOLS.keys())[:20]}...")

    params = await request.json()
    handler = TOOLS[tool_name]["handler"]

    start = time.time()
    log.info(f"[{tool_name}] Called with params: {list(params.keys())}")

    try:
        result = handler(params)
        elapsed = time.time() - start
        log.info(f"[{tool_name}] OK in {elapsed:.2f}s")
        return {"result": result, "elapsed_seconds": round(elapsed, 2)}
    except Exception as e:
        elapsed = time.time() - start
        tb = traceback.format_exc()
        log.error(f"[{tool_name}] FAIL in {elapsed:.2f}s: {e}\n{tb}")
        raise HTTPException(500, detail={"error": str(e), "traceback": tb[:1000], "elapsed": round(elapsed, 2)})

# --- Startup/shutdown ---
@app.on_event("startup")
async def startup():
    build_log("SERVER", "START", f"GPU backend starting on port {os.environ.get('PORT', 35677)}")

@app.on_event("shutdown")
async def shutdown():
    build_log("SERVER", "STOP")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 35677))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
