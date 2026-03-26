export type BackendType = "gpu-local" | "cpu-local" | "cloud-api" | "llm-api";
interface BackendCallOptions {
    backend: BackendType;
    endpoint: string;
    payload: Record<string, unknown>;
    timeoutMs?: number;
}
export declare function callBackend(opts: BackendCallOptions): Promise<unknown>;
export {};
