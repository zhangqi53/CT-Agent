# CT-Agent GPU Backend
# Port: 35677
# Tools: ~68 GPU-based medical CT analysis tools
#
# Build:
#   docker build -t ct-agent-gpu -f Dockerfile . 2>&1 | tee /tmp/gpu-build.log
#
# Run:
#   docker run --gpus all -p 35677:35677 -v /data/models:/app/models ct-agent-gpu

FROM nvcr.io/nvidia/pytorch:24.05-py3

LABEL maintainer="CT-Agent Team"
LABEL description="GPU backend for CT medical image analysis tools"

WORKDIR /app

# --- Build log setup ---
RUN mkdir -p /app/logs && \
    echo "[$(date -Iseconds)] [BUILD] [DOCKERFILE] START" >> /app/logs/build.log

# --- System deps ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    git wget curl libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* \
    && echo "[$(date -Iseconds)] [BUILD] [SYSTEM_DEPS] OK" >> /app/logs/build.log

# --- Python deps (pip-installable tools) ---
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 2>&1 | tee /app/logs/pip-install.log \
    && echo "[$(date -Iseconds)] [BUILD] [PIP_INSTALL] OK" >> /app/logs/build.log \
    || (echo "[$(date -Iseconds)] [BUILD] [PIP_INSTALL] FAIL" >> /app/logs/build.log && exit 1)

# --- Clone GitHub-only tools ---
RUN mkdir -p /app/tools && \
    echo "[$(date -Iseconds)] [BUILD] [GIT_CLONE] START" >> /app/logs/build.log

# Each clone in its own RUN so build log tracks which one fails
RUN git clone --depth 1 https://github.com/SeuTao/RSNA2019_Intracranial-Hemorrhage-Detection.git /app/tools/rsna_ich 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [rsna_ich] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [rsna_ich] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/msharrock/deepbleed.git /app/tools/deepbleed 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [deepbleed] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [deepbleed] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/marshuang80/penet.git /app/tools/penet 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [penet] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [penet] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/MIC-DKFZ/LesionLocator.git /app/tools/lesionlocator 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [lesionlocator] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [lesionlocator] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/jun-sato/sato_j-mid_ad.git /app/tools/sato_anomaly 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [sato_anomaly] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [sato_anomaly] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/han-liu/PanDx.git /app/tools/pandx 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [pandx] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [pandx] CLONE_FAIL" >> /app/logs/build.log

RUN git clone --depth 1 https://github.com/ibrahimethemhamamci/CT-CLIP.git /app/tools/ct_clip 2>&1 | tail -1 \
    && echo "[$(date -Iseconds)] [BUILD] [ct_clip] CLONED" >> /app/logs/build.log \
    || echo "[$(date -Iseconds)] [BUILD] [ct_clip] CLONE_FAIL" >> /app/logs/build.log

RUN echo "[$(date -Iseconds)] [BUILD] [GIT_CLONE] DONE" >> /app/logs/build.log

# --- Copy server code ---
COPY server.py /app/server.py

# --- Final build log entry ---
RUN echo "[$(date -Iseconds)] [BUILD] [DOCKERFILE] COMPLETE" >> /app/logs/build.log

# --- Health check ---
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:35677/health || exit 1

EXPOSE 35677

ENV PORT=35677
ENV LOG_DIR=/app/logs
ENV PYTHONPATH=/app/tools

CMD ["python", "server.py"]
