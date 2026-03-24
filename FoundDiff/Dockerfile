# 1. 霸王硬上弓：直接使用你本地 3 年前缓存的镜像
FROM m.daocloud.io/docker.io/pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /app

# 2. 换源并【直接从 NVIDIA 官方获取 CUDA 编译器】（因为阿里云把老版本删了）
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y gnupg2 curl ca-certificates && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub | apt-key add - && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /" > /etc/apt/sources.list.d/cuda.list && \
    apt-get update && apt-get install -y \
    git \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    cuda-nvcc-11-6 \
    cuda-cudart-dev-11-6 \
    && rm -rf /var/lib/apt/lists/*

# 3. 告诉 pip 编译器装在哪了
ENV CUDA_HOME=/usr/local/cuda-11.6

# 4. 安装基础依赖（【严禁擅自升级】强行锁死 torch 1.13.1）
# 4. 安装基础依赖（融合了你加的 lmdb/matplotlib，以及保命的 transformers 降级）
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    torch==1.13.1 \
    torchvision==0.14.1 \
    Pillow \
    numpy==1.23.5 \
    einops \
    packaging \
    kornia \
    Augmentor \
    opencv-python-headless \
    lpips \
    accelerate \
    ema_pytorch \
    open_clip_torch \
    tqdm \
    ipdb \
    PyWavelets \
    lmdb \
    scikit-image \
    matplotlib \
    transformers==4.28.1

# 4.5 从 GitHub 强制安装 OpenAI 官方 CLIP 模型（关键环节！）
RUN pip install --no-cache-dir git+https://github.com/openai/CLIP.git

# 5. 【关键降级】适配古老的 PyTorch 1.13，防止编译冲突
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    --no-build-isolation \
    torch==1.13.1 \
    causal-conv1d==1.1.0 \
    mamba-ssm==1.1.0

# 6. 拉取官方代码
RUN git clone https://github.com/hao1635/FoundDiff.git /app/FoundDiff

RUN find /app/FoundDiff -type f -name "*.py" -exec sed -i "s/'Dose-CLIP.pth'/'DA-CLIP.pth'/g" {} + && \
    find /app/FoundDiff -type f -name "*.py" -exec sed -i 's/import wandb/# import wandb/g' {} + && \
    # 精准匹配：只替换前面有 4 个空格且独占一行的 folder,
    sed -i "s/^    folder,/    '.',/g" /app/FoundDiff/train.py && \
    sed -i 's/\/\/data/\/data/g' /app/FoundDiff/data/dose_dataset.py

# 8. 放入 Biomni 智能体脚本 (如果你之前写了的话)
 COPY agent_wrapper.py /app/FoundDiff/

WORKDIR /app/FoundDiff

ENTRYPOINT ["python", "agent_wrapper.py"]