import os
import subprocess
import json
import scipy.io
import numpy as np
import time

def evaluate_ct_quality() -> str:
    """
    运行 PR-IQA 工具，批量评估数据库中默认的 152 张 CT 影像。
    返回：包含 152 张图融合打分结果的 JSON 总结。
    """
    result_file = "/home/liuyiwei/PR-IQA/Result/score_3dgr.mat"
    
    # 获取当前用户的 UID 和 GID
    uid = os.getuid()
    gid = os.getgid()

    # 在 Docker 命令中加入 -u 参数，强制 Docker 以当前宿主机用户的身份运行
    # 这样生成的文件所有者就是你，就不会有权限问题了
    cmd = [
        "docker", "run", "--rm", "--gpus", "all",
        "-u", f"{uid}:{gid}",  # <--- 解决权限的核心！
        "-v", "/home/liuyiwei/PR-IQA:/home/liuyiwei/PR-IQA",
        "-v", "/home/liuyiwei/PR-IQA/data:/app/data",
        "-v", "/home/liuyiwei/PR-IQA:/app",
        "-w", "/app",
        "pr-iqa:v1",
        "python", "test_demo.py"
    ]

    try:
        # 记录运行前的时间，防止读到老文件
        start_time = time.time()
        
        # 启动 Docker
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        if os.path.exists(result_file):
            # 检查文件是否是刚生成的（修改时间在启动时间之后）
            file_mtime = os.path.getmtime(result_file)
            if file_mtime < start_time:
                return f"Error: Docker 运行了，但 {result_file} 没有更新。可能是代码内部报错了。日志: {result.stdout}"

            try:
                # 读取 .mat 文件 (此时已经有权限了)
                mat_data = scipy.io.loadmat(result_file)
                fuse_scores = mat_data['score_fuse'].flatten().tolist()
                
                top_indices = np.argsort(fuse_scores)[::-1]
                top_5 = {f"imglow_{idx+1:04d}": round(fuse_scores[idx], 4) for idx in top_indices[:5]}
                
                summary = {
                    "status": "success",
                    "total_images_processed": len(fuse_scores),
                    "average_score": round(sum(fuse_scores) / len(fuse_scores), 4),
                    "top_5_best_images": top_5
                }
                return json.dumps(summary, ensure_ascii=False, indent=2)
                
            except Exception as e:
                return f"Error: Python 解析 {result_file} 失败: {e}"
        else:
            return f"Error: Docker 未生成结果。日志: {result.stdout}"

    except subprocess.CalledProcessError as e:
        return f"Error: Docker 执行失败。错误日志: {e.stderr}"