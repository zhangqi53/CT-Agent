import { log } from "./logger.js";

export type BackendType = "gpu-local" | "cpu-local" | "cloud-api" | "llm-api";

interface BackendCallOptions {
  backend: BackendType;
  endpoint: string;
  payload: Record<string, unknown>;
  timeoutMs?: number;
}

const BACKEND_URLS: Record<string, string> = {
  "gpu-local": process.env.GPU_BACKEND_URL ?? "http://localhost:35677",
  "cpu-local": process.env.CPU_BACKEND_URL ?? "http://localhost:35678",
};

export async function callBackend(opts: BackendCallOptions): Promise<unknown> {
  const { backend, endpoint, payload, timeoutMs = 300_000 } = opts;
  const startTime = Date.now();

  log("INFO", "BACKEND", `Calling ${backend}/${endpoint}`, { payloadKeys: Object.keys(payload) });

  try {
    let url: string;
    let headers: Record<string, string> = { "Content-Type": "application/json" };

    if (backend === "gpu-local" || backend === "cpu-local") {
      url = `${BACKEND_URLS[backend]}/${endpoint}`;
    } else if (backend === "cloud-api") {
      url = endpoint; // 完整 URL
      const apiKey = process.env.HF_API_TOKEN;
      if (apiKey) headers["Authorization"] = `Bearer ${apiKey}`;
    } else if (backend === "llm-api") {
      url = endpoint;
      const apiKey = process.env.LLM_API_KEY;
      if (apiKey) headers["Authorization"] = `Bearer ${apiKey}`;
    } else {
      throw new Error(`Unknown backend type: ${backend}`);
    }

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);

    const resp = await fetch(url, {
      method: "POST",
      headers,
      body: JSON.stringify(payload),
      signal: controller.signal,
    });

    clearTimeout(timer);
    const elapsed = Date.now() - startTime;

    if (!resp.ok) {
      const body = await resp.text();
      log("ERROR", "BACKEND", `${backend}/${endpoint} returned ${resp.status}`, { elapsed, body: body.slice(0, 500) });
      throw new Error(`Backend ${backend}/${endpoint} returned ${resp.status}: ${body.slice(0, 200)}`);
    }

    const result = await resp.json();
    log("INFO", "BACKEND", `${backend}/${endpoint} OK`, { elapsed });
    return result;
  } catch (err) {
    const elapsed = Date.now() - startTime;
    const message = err instanceof Error ? err.message : String(err);
    log("ERROR", "BACKEND", `${backend}/${endpoint} failed`, { elapsed, error: message });
    throw err;
  }
}
