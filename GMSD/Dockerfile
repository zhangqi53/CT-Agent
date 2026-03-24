# 1. 基础镜像：南大源限制了外网 (403)，我们切回 DaoCloud！(runtime 镜像较小，不会断流)
FROM m.daocloud.io/docker.io/pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /app

# 2. 换源神技：Ubuntu 走阿里云，加装 https 支持包
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y git libgl1-mesa-glx libglib2.0-0 build-essential pkg-config libhdf5-dev apt-transport-https ca-certificates

# 3. 终极一击：从 NVIDIA 官方 CDN 秒拉 CUDA 11.6 碎块包！集齐所有 PyTorch 编译所需头文件！
RUN echo "deb [trusted=yes] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /" > /etc/apt/sources.list.d/cuda.list && \
    apt-get update && \
    apt-get install -y \
    cuda-nvcc-11-6 \
    cuda-cudart-dev-11-6 \
    libcublas-dev-11-6 \
    libcusolver-dev-11-6 \
    libcusparse-dev-11-6 \
    libcurand-dev-11-6 \
    libcufft-dev-11-6 \
    && rm -rf /var/lib/apt/lists/*

# 4. 指定编译器路径，让 PyTorch 的 JIT 实时编译精准找到它
ENV CUDA_HOME=/usr/local/cuda-11.6
ENV PATH=${CUDA_HOME}/bin:${PATH}

# 5. Pip 秒杀所有 Python 包 (彻底踢开 Conda，把 astra-toolbox 也交给 pip 秒装)
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    scikit-image pydicom opencv-python-headless pandas ml-collections \
    "tensorflow<2.12.0" tensorflow-probability==0.19.0 tensorflow-gan tensorflow-datasets \
    ninja nvidia-ml-py jax jaxlib "numpy<2.0.0" scipy matplotlib h5py==3.8.0 astra-toolbox

# 6. 复制代码与安装 ODL
COPY . /app/
RUN pip install --no-cache-dir --no-deps /app/odl && \
    rm -rf /app/odl

# 7. 统一入口
ENTRYPOINT ["python", "biomni_wrapper.py"]