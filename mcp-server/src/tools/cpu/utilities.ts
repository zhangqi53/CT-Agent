import { registerTool } from "../../types/tool-registry.js";

registerTool({
  name: "dicom_to_nifti",
  description: "Convert DICOM series to NIfTI format with orientation normalization.",
  inputSchema: {
    type: "object",
    properties: {
      dicom_dir: { type: "string", description: "Path to DICOM directory" },
      output_path: { type: "string", description: "Output NIfTI file path" },
    },
    required: ["dicom_dir"],
  },
  backend: "cpu-local",
  endpoint: "tools/dicom2nifti",
  category: "adapter",
  bodyRegions: ["全身"],
  paper: "dcm2niix / dicom2nifti",
  github: "https://github.com/icometrix/dicom2nifti",
});

registerTool({
  name: "window_level",
  description: "Apply window/level transformation to CT volume. Supports presets (lung, mediastinum, bone, liver, brain, soft_tissue, stroke, subdural) or custom WW/WL.",
  inputSchema: {
    type: "object",
    properties: {
      volume_path: { type: "string" },
      preset: { type: "string", enum: ["lung", "mediastinum", "bone", "liver", "brain", "soft_tissue", "stroke", "subdural"] },
      custom_ww: { type: "number" },
      custom_wl: { type: "number" },
    },
    required: ["volume_path"],
  },
  backend: "cpu-local",
  endpoint: "tools/window_level",
  category: "adapter",
  bodyRegions: ["全身"],
  paper: "SimpleITK IntensityWindowing",
  github: "https://github.com/SimpleITK/SimpleITK",
});

registerTool({
  name: "radiomics_features",
  description: "Extract 1500+ radiomics features (shape, first-order, texture GLCM/GLRLM/GLSZM/GLDM) from a CT volume + segmentation mask.",
  inputSchema: {
    type: "object",
    properties: {
      volume_path: { type: "string" },
      mask_path: { type: "string" },
      feature_classes: {
        type: "array",
        items: { type: "string", enum: ["shape", "firstorder", "glcm", "glrlm", "glszm", "gldm", "ngtdm"] },
        description: "Feature classes to extract. Default: all.",
      },
    },
    required: ["volume_path", "mask_path"],
  },
  backend: "cpu-local",
  endpoint: "tools/pyradiomics",
  category: "measurement",
  bodyRegions: ["全身"],
  paper: "van Griethuysen et al., Cancer Research 2017",
  github: "https://github.com/AIM-Harvard/pyradiomics",
});

registerTool({
  name: "image_registration",
  description: "Register two CT volumes using rigid, affine, or SyN deformable registration. Returns aligned volume + transformation field.",
  inputSchema: {
    type: "object",
    properties: {
      fixed_path: { type: "string", description: "Fixed (baseline) volume" },
      moving_path: { type: "string", description: "Moving (follow-up) volume" },
      method: { type: "string", enum: ["rigid", "affine", "syn"], default: "affine" },
    },
    required: ["fixed_path", "moving_path"],
  },
  backend: "cpu-local",
  endpoint: "tools/antspy_register",
  category: "registration",
  bodyRegions: ["全身"],
  paper: "Avants et al., NeuroImage 2011",
  github: "https://github.com/ANTsX/ANTsPy",
});

registerTool({
  name: "connected_component_filter",
  description: "Post-process segmentation mask: remove small objects, keep largest K components, filter by volume threshold.",
  inputSchema: {
    type: "object",
    properties: {
      mask_path: { type: "string" },
      min_volume_ml: { type: "number", default: 0.5, description: "Minimum component volume in mL" },
      keep_largest_k: { type: "integer", description: "Keep only K largest components" },
    },
    required: ["mask_path"],
  },
  backend: "cpu-local",
  endpoint: "tools/cc3d_filter",
  category: "adapter",
  bodyRegions: ["全身"],
  paper: "connected-components-3d",
  github: "https://github.com/seung-lab/connected-components-3d",
});

registerTool({
  name: "dicom_metadata_reader",
  description: "Read DICOM metadata tags (patient info, scan parameters, contrast agent, slice thickness, etc.).",
  inputSchema: {
    type: "object",
    properties: {
      dicom_path: { type: "string", description: "Path to DICOM file or directory" },
      tags: {
        type: "array",
        items: { type: "string" },
        description: "Specific DICOM tags to read, e.g. ['PatientID','SliceThickness','ContrastBolusAgent']. Default: common clinical tags.",
      },
    },
    required: ["dicom_path"],
  },
  backend: "cpu-local",
  endpoint: "tools/pydicom_read",
  category: "adapter",
  bodyRegions: ["全身"],
  paper: "pydicom",
  github: "https://github.com/pydicom/pydicom",
});

registerTool({
  name: "fhir_export",
  description: "Export structured analysis results as an HL7 FHIR R4 DiagnosticReport resource.",
  inputSchema: {
    type: "object",
    properties: {
      findings: { type: "object", description: "Structured findings JSON from analysis tools" },
      patient_id: { type: "string" },
      study_uid: { type: "string" },
    },
    required: ["findings"],
  },
  backend: "cpu-local",
  endpoint: "tools/fhir_export",
  category: "adapter",
  bodyRegions: ["全身"],
  paper: "fhirpy + fhir.resources",
  github: "https://github.com/beda-software/fhir-py",
});
