type LogLevel = "INFO" | "WARN" | "ERROR" | "BUILD" | "HEALTH";
export declare function log(level: LogLevel, component: string, message: string, meta?: Record<string, unknown>): void;
export declare function buildLog(step: string, status: "START" | "OK" | "FAIL", detail?: string): void;
export declare function healthLog(component: string, ok: boolean, detail?: string): void;
export {};
