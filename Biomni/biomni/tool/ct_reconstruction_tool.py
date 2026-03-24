import os
import json
import subprocess


def evaluate_ct_quality_with_3dgr(input_path: str, output_dir: str, views: int = 40) -> dict:
    """运行 3DGR-CT Docker 容器进行 CT 图像去噪与重建，并返回客观的图像质量评价指标。
    
    该工具会将本地的低剂量 CT 图像输入给 3DGR-CT 模型进行重建，并在输出目录中提取
    包含 MSE, PSNR, SSIM 等图像质量评价指标的结果，供大模型 (LLM-as-a-judge) 评估使用。

    Parameters
    ----------
    input_path : str
        宿主机上待处理 CT 图像文件 (如 test_data/input/chest_data.npz) 的相对路径。
    output_dir : str
        宿主机上期望输出重建后图像及 metrics.json 评估报告的相对路径。
    views : int
        重建使用的投影视图数量，默认值为 40。

    Returns
    -------
    dict
        包含执行状态 (success) 以及提取到的客观指标 (metrics) 的字典。
    """
    uid = os.getuid()
    gid = os.getgid()

    # 1. 宿主机侧：获取当前运行环境的绝对路径，等同于命令里的 $(pwd)
    current_pwd = os.getcwd()
    
    # 确保宿主机上的输出目录存在，防止写入失败
    os.makedirs(output_dir, exist_ok=True)

    # 2. 容器侧：构建容器内部能识别的绝对路径
    container_input = f"/app/{input_path}" if not input_path.startswith('/app') else input_path
    container_output = f"/app/{output_dir}" if not output_dir.startswith('/app') else output_dir

    # 3. 构建完全对齐你环境的 Docker 运行命令
    cmd = [
        "docker", "run", "--rm",
        "-u", f"{uid}:{gid}" ,
        "--gpus", "all",
        "--ipc=host",
        "-e", "PYTHONUNBUFFERED=1",
        "-e", "MAX_JOBS=1",
        "-e", "TORCH_CUDA_ARCH_LIST=7.5;8.0;8.6;8.9+PTX",

        "-e", "TORCH_EXTENSIONS_DIR=/tmp/torch_ext",
        "-e", "XDG_CACHE_HOME=/tmp/cache",
        
        # 【关键修改 1】：只挂载 test_data 文件夹，保护容器内的 /app 代码不被覆盖
        #"-v", f"{current_pwd}/test_data:/app/test_data",
        "-v", f"{os.getcwd()}/test_data:/app/test_data",

        "-w", "/app",
        
        # 【关键修改 2】：使用包含了正确路径代码的新镜像 v2
        "biomni-tool-3dgr-ct:v3", 
        
        "--input_dir", container_input,
        "--output_dir", container_output,
        "--views", str(views)
    ]

    try:
        # 执行容器命令，捕获输出
        print(f"正在启动 3DGR-CT 容器，执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 4. 提取指标：尝试读取容器跑完后在宿主机生成的 metrics.json
        metrics_file = os.path.join(current_pwd, output_dir, "metrics.json")
        if os.path.exists(metrics_file):
            with open(metrics_file, 'r') as f:
                metrics_data = json.load(f)
            return {
                "success": True,
                "message": "CT 重建完成。客观评估指标已提取。",
                "metrics": metrics_data
            }
        else:
            # 如果没找到 json，就把标准输出甩给大模型，让它自己找数值
            return {
                "success": True,
                "message": "CT 重建完成，但未找到 metrics.json。以下是执行日志：",
                "stdout": result.stdout
            }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": f"3DGR-CT 容器执行失败。错误日志:\n{e.stderr if e.stderr else e.stdout}"
        }