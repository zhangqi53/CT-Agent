# 1. 使用 Python 3.13 的官方轻量级镜像
FROM python:3.13-slim

# 2. 设置工作目录
WORKDIR /app

# 3. 安装系统级依赖
# python3-tk: 解决 from tkinter import _flatten 报错
# libgl1/libglib2: 提供底层图像处理库支持，修正了新版 Debian 中的包名
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 4. 升级 pip
RUN pip install --no-cache-dir --upgrade pip

# 5. 安装 PyTorch 和 Torchvision (包含 GPU 支持)
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 6. 安装其他 Python 依赖包
RUN pip install --no-cache-dir \
    numpy \
    scipy \
    h5py \
    Pillow \
    ipdb

# 7. 将当前目录下所有代码复制进容器的 /app 目录
COPY . /app/

# 8. 设置容器启动默认命令
CMD ["python", "main.py"]