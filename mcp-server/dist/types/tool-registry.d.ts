import type { BackendType } from "../utils/call-backend.js";
export interface ToolDef {
    name: string;
    description: string;
    inputSchema: Record<string, unknown>;
    backend: BackendType;
    endpoint: string;
    category: "segmentation" | "detection" | "classification" | "measurement" | "registration" | "report" | "nlp" | "adapter" | "staging" | "tracking" | "vlm";
    bodyRegions: string[];
    paper: string;
    github: string;
}
export declare const TOOL_REGISTRY: ToolDef[];
export declare function registerTool(def: ToolDef): void;
