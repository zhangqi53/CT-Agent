# 1. 使用你本地现成的 PyTorch 镜像
FROM m.daocloud.io/docker.io/pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /app

# 2. 换源并安装系统基础库 (git 是拉取代码所必需的，libgl 用于底层图像处理支持)
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. 直接安装 wrapper 处理图像实际需要的库，无视官方报错的 environment.yml
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    torchvision \
    Pillow

# 4. 克隆最新的官方仓库
RUN git clone https://github.com/sypsyp97/Eagle_Loss.git /app/Eagle_Loss

# 5. 将宿主机上的 wrapper 脚本直接放入官方源码根目录
COPY agent_wrapper.py /app/Eagle_Loss/

# 6. 切换工作目录到源码目录
WORKDIR /app/Eagle_Loss

# 7. 设定智能体调用入口
# 此时 agent_wrapper.py 就在 eagle_loss 文件夹旁边，Python 会直接将其作为本地包导入
ENTRYPOINT ["python", "agent_wrapper.py"]