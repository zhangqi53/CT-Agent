# 基于原来的 v1 镜像
FROM biomni-tool-3dgr-ct:v1

# 切换为 root 用户以确保有权限覆盖文件
USER root

# 把你修改好路径的代码，复制进容器的 /app 目录
# 巧妙之处：Docker 的 COPY 只会覆盖同名文件，不会删掉容器里原本存在的 run_reconstruction.py
COPY ./3DGR-CT/3DGR-CT/ /app/

# （可选）重置权限，确保执行顺畅
RUN chmod -R 777 /app
