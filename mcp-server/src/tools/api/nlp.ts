import { registerTool } from "../../types/tool-registry.js";

registerTool({
  name: "report_ner",
  description: "Extract entities (anatomy, observation, assertion status) and relations from CT radiology reports. Covers chest CT, abdomen/pelvis CT, brain MRI. F1=0.94 NER.",
  inputSchema: {
    type: "object",
    properties: {
      report_text: { type: "string", description: "Radiology report text" },
      model: { type: "string", enum: ["radgraph", "radgraph-xl"], default: "radgraph-xl" },
    },
    required: ["report_text"],
  },
  backend: "cloud-api",
  endpoint: "https://api-inference.huggingface.co/models/StanfordAIMI/radgraph-xl",
  category: "nlp",
  bodyRegions: ["全身"],
  paper: "Jain et al., ACL 2024",
  github: "https://github.com/Stanford-AIMI/radgraph",
});

registerTool({
  name: "measurement_extractor",
  description: "Extract structured measurement data (lesion size, location, RECIST values) from radiology report text. 93.7% accuracy on CT reports.",
  inputSchema: {
    type: "object",
    properties: {
      report_text: { type: "string" },
      schema: { type: "object", description: "Pydantic-style schema defining what to extract" },
    },
    required: ["report_text"],
  },
  backend: "llm-api",
  endpoint: "https://api.openai.com/v1/chat/completions", // 或 Ollama
  category: "nlp",
  bodyRegions: ["全身"],
  paper: "van Driel et al., JAMIA Open 2025",
  github: "https://github.com/DIAGNijmegen/llm_extractinator",
});

registerTool({
  name: "negation_detector",
  description: "Detect negation and uncertainty in radiology report sentences. Rule-based, modality-agnostic.",
  inputSchema: {
    type: "object",
    properties: {
      text: { type: "string" },
    },
    required: ["text"],
  },
  backend: "cpu-local",
  endpoint: "tools/medspacy_negation",
  category: "nlp",
  bodyRegions: ["全身"],
  paper: "Eyre et al., AMIA 2021; Peng et al., AMIA 2018",
  github: "https://github.com/medspacy/medspacy",
});
