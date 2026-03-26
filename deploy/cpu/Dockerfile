# CT-Agent CPU Backend
# Port: 35678
# Tools: ~32 CPU-based utility/NLP/adapter tools

FROM python:3.10-slim

LABEL maintainer="CT-Agent Team"
LABEL description="CPU backend for CT utility, NLP, and adapter tools"

WORKDIR /app

RUN mkdir -p /app/logs && \
    echo "[$(date -Iseconds)] [BUILD] [DOCKERFILE] START" >> /app/logs/build.log

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* \
    && echo "[$(date -Iseconds)] [BUILD] [SYSTEM_DEPS] OK" >> /app/logs/build.log

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 2>&1 | tee /app/logs/pip-install.log \
    && echo "[$(date -Iseconds)] [BUILD] [PIP_INSTALL] OK" >> /app/logs/build.log \
    || (echo "[$(date -Iseconds)] [BUILD] [PIP_INSTALL] FAIL" >> /app/logs/build.log && exit 1)

COPY server.py /app/server.py

RUN echo "[$(date -Iseconds)] [BUILD] [DOCKERFILE] COMPLETE" >> /app/logs/build.log

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:35678/health || exit 1

EXPOSE 35678

ENV PORT=35678
ENV LOG_DIR=/app/logs

CMD ["python", "server.py"]
