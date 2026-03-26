import type { BackendType } from "../utils/call-backend.js";

export interface ToolDef {
  name: string;
  description: string;
  inputSchema: Record<string, unknown>;
  backend: BackendType;
  endpoint: string;
  category: "segmentation" | "detection" | "classification" | "measurement" | "registration" | "report" | "nlp" | "adapter" | "staging" | "tracking" | "vlm";
  bodyRegions: string[]; // 验证过的部位
  paper: string;
  github: string;
}

export const TOOL_REGISTRY: ToolDef[] = [];

export function registerTool(def: ToolDef): void {
  TOOL_REGISTRY.push(def);
}
