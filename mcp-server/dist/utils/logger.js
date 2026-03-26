import { appendFileSync, mkdirSync, existsSync } from "fs";
import { join } from "path";
const LOG_DIR = process.env.LOG_DIR ?? "./logs";
const LOG_FILE = join(LOG_DIR, `mcp-${new Date().toISOString().slice(0, 10)}.log`);
if (!existsSync(LOG_DIR)) {
    mkdirSync(LOG_DIR, { recursive: true });
}
function formatEntry(level, component, message, meta) {
    const ts = new Date().toISOString();
    const base = `[${ts}] [${level}] [${component}] ${message}`;
    return meta ? `${base} ${JSON.stringify(meta)}` : base;
}
export function log(level, component, message, meta) {
    const entry = formatEntry(level, component, message, meta);
    console.error(entry); // MCP 协议用 stderr 输出日志
    appendFileSync(LOG_FILE, entry + "\n");
}
export function buildLog(step, status, detail) {
    const buildFile = join(LOG_DIR, "build.log");
    const entry = formatEntry("BUILD", step, status, detail ? { detail } : undefined);
    appendFileSync(buildFile, entry + "\n");
    console.error(entry);
}
export function healthLog(component, ok, detail) {
    log(ok ? "INFO" : "ERROR", "HEALTH", `${component}: ${ok ? "OK" : "FAIL"}`, detail ? { detail } : undefined);
}
//# sourceMappingURL=logger.js.map