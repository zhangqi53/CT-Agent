import os
import subprocess
import json
import scipy.io
import numpy as np
import time

def lama_ct_reconstruction(input_path: str, output_path: str, n_views: int = 64, dataset: str = "mayo") -> str:
    """
    使用 LAMA（Learned Alternating Minimization Algorithm）对稀疏视角 CT 正弦图进行高质量图像重建。
    
    Parameters
    ----------
    input_path : str
        输入稀疏视角 CT 正弦图路径（.mat 格式，shape: n_views x 512）
    output_path : str
        重建结果保存路径（.mat 格式，重建图像 shape: 256 x 256）
    n_views : int
        稀疏视角数量，支持 64 或 128，默认 64
    dataset : str
        数据集类型，支持 mayo 或 NBIA，默认 mayo

    Returns
    -------
    str
        包含重建结果信息的 JSON 字符串
    """
    output_dir = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(output_dir, exist_ok=True)

    lama_root = "/home/liuyiwei/LAMA-Learned-Alternating-Minimization-Algorithm"
    if input_path.startswith(lama_root):
        container_input = "/app" + input_path[len(lama_root):]
    else:
        container_input = input_path

    cmd = [
        "/usr/bin/docker", "run", "--rm", "--gpus", "all",
        "-v", f"{lama_root}:/app",
        "-v", f"{output_dir}:/output",
        "biomni-lama-tool:v1",
        "--input_path", container_input,
        "--output_path", f"/output/{os.path.basename(output_path)}",
        "--views", str(n_views),
        "--dataset", dataset
    ]

    try:
        start_time = time.time()
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            check=True, timeout=600
        )

        # 修复输出文件权限
        subprocess.run([
            "/usr/bin/docker", "run", "--rm",
            "-v", f"{output_dir}:/output",
            "--entrypoint", "chmod",
            "biomni-lama-tool:v1",
            "644", f"/output/{os.path.basename(output_path)}"
        ], capture_output=True)

        if os.path.exists(output_path):
            file_mtime = os.path.getmtime(output_path)
            if file_mtime < start_time:
                return f"Error: Docker 运行了，但 {output_path} 没有更新。stdout: {result.stdout}"

            try:
                mat_data = scipy.io.loadmat(output_path)
                recon_img = mat_data['data']

                psnr_val, ssim_val = None, None
                for line in result.stdout.splitlines():
                    if "avg PSNR" in line:
                        psnr_val = line.strip()
                    if "avg SSIM" in line:
                        ssim_val = line.strip()

                summary = {
                    "status": "success",
                    "input_path": input_path,
                    "output_path": output_path,
                    "n_views": n_views,
                    "dataset": dataset,
                    "output_shape": list(recon_img.shape),
                    "value_range": [round(float(recon_img.min()), 4), round(float(recon_img.max()), 4)],
                    "metrics": {"psnr": psnr_val, "ssim": ssim_val}
                }
                return json.dumps(summary, ensure_ascii=False, indent=2)

            except Exception as e:
                return f"Error: 解析输出文件失败: {e}"
        else:
            return f"Error: Docker 未生成结果文件。stdout: {result.stdout}"

    except subprocess.CalledProcessError as e:
        return f"Error: Docker 执行失败。returncode={e.returncode} stdout={e.stdout} stderr={e.stderr}"
    except FileNotFoundError as e:
        return f"Error: 找不到docker命令: {e}"
    except subprocess.TimeoutExpired:
        return "Error: Docker 执行超时（超过600秒）"