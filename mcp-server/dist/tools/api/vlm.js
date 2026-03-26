import { registerTool } from "../../types/tool-registry.js";
registerTool({
    name: "merlin_classify",
    description: "Zero-shot classification of 30 abdominal CT findings + 692 phenotypes using Merlin VLM (Nature 2026). Covers: lower thorax, liver, gallbladder, spleen, pancreas, adrenal, kidney, GI, pelvis, vasculature.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to abdominal CT NIfTI" },
            task: { type: "string", enum: ["classify_30", "phenotype_692", "report", "segment_20"], default: "classify_30" },
        },
        required: ["volume_path"],
    },
    backend: "cloud-api",
    endpoint: "https://api.replicate.com/v1/predictions", // 或 HuggingFace Inference Endpoint
    category: "vlm",
    bodyRegions: ["肝脏", "胆囊/胆道", "胰腺", "脾脏", "肾脏/肾上腺", "胃肠道", "盆腔", "纵隔/心脏"],
    paper: "Blankemeier et al., Nature 2026",
    github: "https://github.com/StanfordMIMI/Merlin",
});
registerTool({
    name: "radfm_diagnosis",
    description: "General-purpose radiology VLM for diagnosis, VQA, report generation, and differential diagnosis. Supports 2D+3D CT across all body regions.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to CT NIfTI (2D slice or 3D volume)" },
            question: { type: "string", description: "Clinical question or task instruction" },
            clinical_text: { type: "string", description: "Optional: clinical history / prior reports" },
        },
        required: ["volume_path", "question"],
    },
    backend: "cloud-api",
    endpoint: "https://api.replicate.com/v1/predictions",
    category: "vlm",
    bodyRegions: ["全身"],
    paper: "Wu et al., Nature Communications 2025",
    github: "https://github.com/chaoyi-wu/RadFM",
});
registerTool({
    name: "medgemma_analyze",
    description: "Google MedGemma 1.5: 3D CT VQA and report generation. Supports native 3D volume input for head, chest, abdomen.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string" },
            prompt: { type: "string", description: "Clinical question or report instruction" },
        },
        required: ["volume_path", "prompt"],
    },
    backend: "cloud-api",
    endpoint: "https://generativelanguage.googleapis.com/v1beta/models/medgemma-1.5-4b-it:generateContent",
    category: "vlm",
    bodyRegions: ["脑/颅内", "肺", "纵隔/心脏", "肝脏", "腹部"],
    paper: "Google, 2025",
    github: "https://huggingface.co/google/medgemma-1.5-4b-it",
});
registerTool({
    name: "ct_chat_vqa",
    description: "CT-CHAT: Visual question answering and report generation for chest CT. Based on CT-CLIP + LLaVA architecture.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to chest CT NIfTI" },
            question: { type: "string", description: "Question about the CT scan" },
        },
        required: ["volume_path", "question"],
    },
    backend: "cloud-api",
    endpoint: "https://api-inference.huggingface.co/models/ibrahimethemhamamci/CT-CHAT",
    category: "vlm",
    bodyRegions: ["肺", "纵隔/心脏"],
    paper: "Hamamci et al., Nature BME 2025",
    github: "https://github.com/ibrahimethemhamamci/CT-CHAT",
});
registerTool({
    name: "brain_report_generator",
    description: "Generate structured 4-section radiology report from 3D brain CT. F1=0.71, 74% indistinguishable from human.",
    inputSchema: {
        type: "object",
        properties: {
            volume_path: { type: "string", description: "Path to brain CT NIfTI" },
        },
        required: ["volume_path"],
    },
    backend: "cloud-api",
    endpoint: "https://api-inference.huggingface.co/models/charlierabea/FORTE",
    category: "report",
    bodyRegions: ["脑/颅内"],
    paper: "Rabea et al., Nature Communications 2025",
    github: "https://github.com/charlierabea/FORTE",
});
//# sourceMappingURL=vlm.js.map