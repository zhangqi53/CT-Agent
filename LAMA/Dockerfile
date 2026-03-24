FROM m.daocloud.io/docker.io/pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    pkg-config \
    libhdf5-dev \
    cmake \
    && rm -rf /var/lib/apt/lists/*

RUN conda install -y -c nvidia cuda-nvcc=11.6

ENV CUDA_HOME=/opt/conda
ENV TORCH_CUDA_ARCH_LIST="8.6"

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    scikit-image \
    pydicom \
    opencv-python-headless \
    pandas \
    ml-collections \
    ninja \
    scipy \
    matplotlib \
    h5py==3.8.0 \
    pytorch_msssim \
    "numpy<2.0.0"

RUN git clone https://github.com/xiawj-hub/CTLIB.git /tmp/ctlib && \
    cd /tmp/ctlib && \
    python setup.py install && \
    rm -rf /tmp/ctlib

COPY . /app/

ENTRYPOINT ["python", "agent_wrapper.py"]