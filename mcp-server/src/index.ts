import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { log, buildLog, healthLog } from "./utils/logger.js";
import { callBackend } from "./utils/call-backend.js";
import { TOOL_REGISTRY } from "./types/tool-registry.js";

// --- 注册所有工具模块 ---
import "./tools/gpu/segmentation.js";
import "./tools/cpu/utilities.js";
import "./tools/api/vlm.js";
import "./tools/api/nlp.js";

buildLog("INIT", "START", `Loading ${TOOL_REGISTRY.length} tools`);

const server = new McpServer({
  name: "ct-agent-mcp-server",
  version: "0.1.0",
});

// --- 动态注册所有工具到 MCP ---
for (const tool of TOOL_REGISTRY) {
  const paramShape: Record<string, z.ZodTypeAny> = {};

  // 从 inputSchema.properties 生成 zod schema
  const props = (tool.inputSchema as { properties?: Record<string, { type: string }> }).properties ?? {};
  const required = new Set(
    ((tool.inputSchema as { required?: string[] }).required ?? [])
  );

  for (const [key, spec] of Object.entries(props)) {
    let field: z.ZodTypeAny;
    switch (spec.type) {
      case "number":
        field = z.number();
        break;
      case "integer":
        field = z.number().int();
        break;
      case "boolean":
        field = z.boolean();
        break;
      case "array":
        field = z.array(z.string());
        break;
      case "object":
        field = z.record(z.string(), z.unknown());
        break;
      default:
        field = z.string();
    }
    paramShape[key] = required.has(key) ? field : field.optional();
  }

  server.tool(
    tool.name,
    `${tool.description}\n\n[Paper: ${tool.paper}] [Backend: ${tool.backend}] [Regions: ${tool.bodyRegions.join(", ")}]`,
    paramShape,
    async (params) => {
      const startTime = Date.now();
      log("INFO", tool.name, "Tool called", { params, backend: tool.backend });

      try {
        const result = await callBackend({
          backend: tool.backend,
          endpoint: tool.endpoint,
          payload: params as Record<string, unknown>,
        });

        const elapsed = Date.now() - startTime;
        log("INFO", tool.name, "Tool completed", { elapsed });

        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      } catch (err) {
        const elapsed = Date.now() - startTime;
        const message = err instanceof Error ? err.message : String(err);
        log("ERROR", tool.name, "Tool failed", { elapsed, error: message });

        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify({ error: message, tool: tool.name, elapsed }),
            },
          ],
          isError: true,
        };
      }
    },
  );
}

buildLog("INIT", "OK", `Registered ${TOOL_REGISTRY.length} tools`);

// --- 健康检查资源 ---
server.resource(
  "health",
  "health://status",
  async () => {
    const checks: Record<string, string> = {};

    // 检查各 backend
    for (const backend of ["gpu-local", "cpu-local"] as const) {
      try {
        const resp = await fetch(
          `${backend === "gpu-local" ? process.env.GPU_BACKEND_URL ?? "http://localhost:35677" : process.env.CPU_BACKEND_URL ?? "http://localhost:35678"}/health`,
          { signal: AbortSignal.timeout(5000) },
        );
        checks[backend] = resp.ok ? "OK" : `HTTP ${resp.status}`;
        healthLog(backend, resp.ok);
      } catch {
        checks[backend] = "UNREACHABLE";
        healthLog(backend, false, "Connection failed");
      }
    }

    return {
      contents: [
        {
          uri: "health://status",
          text: JSON.stringify({
            server: "ct-agent-mcp-server",
            version: "0.1.0",
            tools_registered: TOOL_REGISTRY.length,
            backends: checks,
            timestamp: new Date().toISOString(),
          }, null, 2),
          mimeType: "application/json",
        },
      ],
    };
  },
);

// --- 启动 ---
async function main() {
  buildLog("SERVER", "START", "Starting MCP server via stdio");

  const transport = new StdioServerTransport();
  await server.connect(transport);

  log("INFO", "SERVER", `MCP server running with ${TOOL_REGISTRY.length} tools`);
}

main().catch((err) => {
  buildLog("SERVER", "FAIL", err instanceof Error ? err.message : String(err));
  process.exit(1);
});
