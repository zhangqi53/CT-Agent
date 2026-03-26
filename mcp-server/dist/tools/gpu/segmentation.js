import { registerTool } from "../../types/tool-registry.js";
// --- 全身解剖分割 ---
registerTool({
    name: "totalsegmentator",
    description: "Segment 117 anatomical structures in CT (organs, bones, muscles, vessels). Input: NIfTI volume. Output: multi-label NIfTI mask + per-structure volume stats.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to input NIfTI CT volume" },
            task: { type: "string", enum: ["total", "lung_vessels", "cerebral_bleed", "hip_implant", "coronary_arteries", "body_trunc", "pleural_pericard_effusion"], default: "total" },
            fast: { type: "boolean", default: false, description: "Use fast mode (lower resolution, ~15s)" },
            statistics: { type: "boolean", default: true, description: "Output per-structure volume statistics" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/totalsegmentator",
    category: "segmentation",
    bodyRegions: ["全身"],
    paper: "Wasserthal et al., Radiology:AI 2023",
    github: "https://github.com/wasserth/TotalSegmentator",
});
registerTool({
    name: "cads_segmentation",
    description: "Segment 167 anatomical structures in CT (most comprehensive). Input: NIfTI. Output: multi-label NIfTI mask.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to input NIfTI CT volume" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/cads",
    category: "segmentation",
    bodyRegions: ["全身（头→膝）"],
    paper: "Xu et al., arXiv:2507.22953",
    github: "https://github.com/murong-xu/CADS",
});
// --- 肺 ---
registerTool({
    name: "lungmask",
    description: "Robust lung and lobe segmentation on CT, handles pathological lungs (consolidation, effusion, tumors). Output: 5-lobe NIfTI mask.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
            model: { type: "string", enum: ["R231", "LTRCLobes", "R231CovidWeb"], default: "LTRCLobes" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/lungmask",
    category: "segmentation",
    bodyRegions: ["肺"],
    paper: "Hofmanninger et al., Eur Radiol 2020",
    github: "https://github.com/JoHof/lungmask",
});
registerTool({
    name: "lung_nodule_detection",
    description: "Detect lung nodules in CT using 3D RetinaNet. Output: list of 3D bounding boxes with confidence scores.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
            score_threshold: { type: "number", default: 0.5 },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/monai/lung_nodule_ct_detection",
    category: "detection",
    bodyRegions: ["肺"],
    paper: "MONAI Model Zoo, RetinaNet on LUNA16",
    github: "https://github.com/Project-MONAI/model-zoo",
});
// --- 肝脏 ---
registerTool({
    name: "liver_lesion_segmentation",
    description: "Segment liver lesions on multi-phase CT. Output: NIfTI mask of liver + lesion regions.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to input CT (portal venous phase preferred)" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/mullet",
    category: "segmentation",
    bodyRegions: ["肝脏"],
    paper: "Wang et al., iScience 2023",
    github: "https://github.com/shenhai1895/Multi-phase-Liver-Lesion-Segmentation",
});
// --- 脑 ---
registerTool({
    name: "intracranial_hemorrhage_detection",
    description: "Detect and classify intracranial hemorrhage into 5 subtypes (epidural, subdural, subarachnoid, intraparenchymal, intraventricular). AUC 0.988.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/rsna_ich",
    category: "classification",
    bodyRegions: ["脑/颅内"],
    paper: "Wang et al., NeuroImage:Clinical 2021",
    github: "https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection",
});
registerTool({
    name: "ich_segmentation",
    description: "Segment intracranial hemorrhage and quantify volume (mL). Dice 0.914.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/deepbleed",
    category: "segmentation",
    bodyRegions: ["脑/颅内"],
    paper: "Sharrock et al., Neuroinformatics 2021",
    github: "https://github.com/msharrock/deepbleed",
});
// --- 纵向追踪 ---
registerTool({
    name: "lesion_tracker",
    description: "Zero-shot tumor segmentation and longitudinal tracking across baseline and follow-up CT. Supports whole-body. CVPR 2025, autoPET IV champion.",
    inputSchema: {
        type: "object",
        properties: {
            baseline_path: { type: "string", description: "Baseline CT NIfTI" },
            followup_path: { type: "string", description: "Follow-up CT NIfTI" },
            prompt_mask_path: { type: "string", description: "Optional: previous segmentation mask as prompt" },
        },
        required: ["baseline_path", "followup_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/lesionlocator",
    category: "tracking",
    bodyRegions: ["肺", "肝脏", "胰腺", "肾脏", "全身"],
    paper: "Rokuss et al., CVPR 2025",
    github: "https://github.com/MIC-DKFZ/LesionLocator",
});
// --- 多器官异常检测 ---
registerTool({
    name: "multi_organ_anomaly_detection",
    description: "Detect anomalies across 7 abdominal organs (liver, gallbladder, pancreas, spleen, kidney, adrenal, esophagus) with specific findings (cyst, stone, mass, calcification, dilation, etc.). eBioMedicine (Lancet) 2024.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
            organs: {
                type: "array",
                items: { type: "string", enum: ["liver", "gallbladder", "pancreas", "spleen", "kidney", "adrenal", "esophagus"] },
                description: "Which organs to screen. Default: all.",
            },
        },
        required: ["volume_path"],
    },
    backend: "gpu-local",
    endpoint: "tools/sato_anomaly",
    category: "detection",
    bodyRegions: ["肝脏", "胆囊/胆道", "胰腺", "脾脏", "肾脏/肾上腺"],
    paper: "Sato et al., eBioMedicine (Lancet) 2024",
    github: "https://github.com/jun-sato/sato_j-mid_ad",
});
//# sourceMappingURL=segmentation.js.map