#!/usr/bin/env bash
#
# CT-Agent 构建总控脚本
# 用法: ./build.sh [gpu|cpu|gateway|all]
#
# 功能:
#   1. 构建 Docker 镜像（带详细日志）
#   2. 每一步记录时间戳和成功/失败状态
#   3. 构建失败时立即报错并输出日志位置
#   4. 最后输出构建摘要

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEPLOY_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="$DEPLOY_DIR/build-logs"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
SUMMARY_LOG="$LOG_DIR/build-summary-$TIMESTAMP.log"

mkdir -p "$LOG_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() {
    local level=$1 msg=$2
    local ts=$(date -Iseconds)
    echo -e "[$ts] [$level] $msg" | tee -a "$SUMMARY_LOG"
}

build_container() {
    local name=$1
    local context=$2
    local dockerfile=$3
    local build_log="$LOG_DIR/${name}-build-$TIMESTAMP.log"

    log "INFO" "┌── Building ${YELLOW}$name${NC} ──────────────────"
    log "INFO" "│   Context:    $context"
    log "INFO" "│   Dockerfile: $dockerfile"
    log "INFO" "│   Log:        $build_log"

    local start_time=$(date +%s)

    if docker build \
        -t "ct-agent-$name" \
        -f "$dockerfile" \
        "$context" \
        2>&1 | tee "$build_log"; then

        local end_time=$(date +%s)
        local elapsed=$((end_time - start_time))
        log "INFO" "│   ${GREEN}✅ SUCCESS${NC} ($elapsed seconds)"
        log "INFO" "└──────────────────────────────────────"
        return 0
    else
        local end_time=$(date +%s)
        local elapsed=$((end_time - start_time))
        log "ERROR" "│   ${RED}❌ FAILED${NC} ($elapsed seconds)"
        log "ERROR" "│   查看完整日志: $build_log"
        log "ERROR" "│   最后 20 行:"
        tail -20 "$build_log" | while IFS= read -r line; do
            log "ERROR" "│   > $line"
        done
        log "ERROR" "└──────────────────────────────────────"
        return 1
    fi
}

verify_container() {
    local name=$1
    local port=$2

    log "INFO" "验证 $name (port $port)..."

    # Start container temporarily
    local cid
    if [[ "$name" == "gpu" ]]; then
        cid=$(docker run -d --rm --gpus all -p "$port:$port" "ct-agent-$name" 2>/dev/null || echo "")
    else
        cid=$(docker run -d --rm -p "$port:$port" "ct-agent-$name" 2>/dev/null || echo "")
    fi

    if [[ -z "$cid" ]]; then
        log "WARN" "  ${YELLOW}⚠️  容器启动失败（可能缺少 GPU）${NC}"
        return 1
    fi

    # Wait for health check
    local retries=10
    while [[ $retries -gt 0 ]]; do
        if curl -sf "http://localhost:$port/health" > /dev/null 2>&1; then
            local health=$(curl -s "http://localhost:$port/health")
            local tools_loaded=$(echo "$health" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tools_loaded',0))" 2>/dev/null || echo "?")
            local tools_failed=$(echo "$health" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tools_failed',0))" 2>/dev/null || echo "?")

            log "INFO" "  ${GREEN}✅ 健康检查通过${NC}: $tools_loaded 工具加载, $tools_failed 失败"

            # Get build log from container
            local container_build_log=$(curl -s "http://localhost:$port/build-log" 2>/dev/null || echo "{}")
            echo "$container_build_log" > "$LOG_DIR/${name}-runtime-$TIMESTAMP.json"
            log "INFO" "  运行时构建日志: $LOG_DIR/${name}-runtime-$TIMESTAMP.json"

            # Get errors if any
            if [[ "$tools_failed" != "0" && "$tools_failed" != "?" ]]; then
                local errors=$(curl -s "http://localhost:$port/errors" 2>/dev/null || echo "{}")
                log "WARN" "  ${YELLOW}失败的工具:${NC}"
                echo "$errors" | python3 -c "
import sys, json
errors = json.load(sys.stdin)
for name, tb in errors.items():
    print(f'    - {name}: {tb.splitlines()[-1] if tb else \"unknown\"}')
" 2>/dev/null || true
            fi

            docker stop "$cid" > /dev/null 2>&1 || true
            return 0
        fi
        sleep 3
        retries=$((retries - 1))
    done

    log "ERROR" "  ${RED}❌ 健康检查超时${NC}"
    docker logs "$cid" 2>&1 | tail -20 | while IFS= read -r line; do
        log "ERROR" "  > $line"
    done
    docker stop "$cid" > /dev/null 2>&1 || true
    return 1
}

# ============================================================
# MAIN
# ============================================================

TARGET="${1:-all}"

log "INFO" "============================================"
log "INFO" "CT-Agent 构建开始: $TIMESTAMP"
log "INFO" "目标: $TARGET"
log "INFO" "日志目录: $LOG_DIR"
log "INFO" "============================================"

FAILED=0

if [[ "$TARGET" == "all" || "$TARGET" == "gpu" ]]; then
    build_container "gpu" "$DEPLOY_DIR/gpu-main" "$DEPLOY_DIR/gpu-main/Dockerfile" || FAILED=$((FAILED + 1))
fi

if [[ "$TARGET" == "all" || "$TARGET" == "cpu" ]]; then
    build_container "cpu" "$DEPLOY_DIR/cpu" "$DEPLOY_DIR/cpu/Dockerfile" || FAILED=$((FAILED + 1))
fi

if [[ "$TARGET" == "all" || "$TARGET" == "gateway" ]]; then
    build_container "gateway" "$DEPLOY_DIR/.." "$DEPLOY_DIR/gateway/Dockerfile" || FAILED=$((FAILED + 1))
fi

# --- 验证 ---
log "INFO" ""
log "INFO" "============================================"
log "INFO" "构建后验证"
log "INFO" "============================================"

if [[ "$TARGET" == "all" || "$TARGET" == "gpu" ]]; then
    verify_container "gpu" 35677 || true
fi

if [[ "$TARGET" == "all" || "$TARGET" == "cpu" ]]; then
    verify_container "cpu" 35678 || true
fi

# --- 摘要 ---
log "INFO" ""
log "INFO" "============================================"
log "INFO" "构建摘要"
log "INFO" "============================================"
log "INFO" "构建日志目录: $LOG_DIR"
log "INFO" "总控日志: $SUMMARY_LOG"

if [[ $FAILED -eq 0 ]]; then
    log "INFO" "${GREEN}✅ 全部构建成功${NC}"
    log "INFO" ""
    log "INFO" "启动命令:"
    log "INFO" "  cd $DEPLOY_DIR && docker compose up -d"
    log "INFO" ""
    log "INFO" "端口:"
    log "INFO" "  35677 - GPU 后端 (${tools_loaded:-?} 工具)"
    log "INFO" "  35678 - CPU 后端"
    log "INFO" "  35679 - MCP Gateway"
else
    log "ERROR" "${RED}❌ $FAILED 个容器构建失败${NC}"
    log "ERROR" "查看详细日志: ls $LOG_DIR/"
    exit 1
fi
