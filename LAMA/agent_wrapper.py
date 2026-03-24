import argparse
import os
import sys
import shutil
import scipy.io
import numpy as np
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Biomni LAMA Reconstruction Wrapper")
    parser.add_argument("--input_path", type=str, required=True, help="输入正弦图路径 (.mat)")
    parser.add_argument("--output_path", type=str, required=True, help="重建结果保存路径 (.mat)")
    parser.add_argument("--views", type=int, choices=[64, 128], default=64, help="稀疏视图数量")
    parser.add_argument("--dataset", type=str, default="mayo", help="数据集名称")
    args = parser.parse_args()

    ROOT = Path("/app")
    dataset = args.dataset
    n_views = args.views
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    test_sino_dir = ROOT / "dataset" / dataset / "test" / "FullViewNoiseless"
    test_sino_dir.mkdir(parents=True, exist_ok=True)
    dest = test_sino_dir / "data001.mat"
    if input_path.resolve() != dest.resolve():
        shutil.copy(str(input_path), str(dest))
    print(f">>> 输入文件已复制到 {dest}")

    for d in ["ground_truth", f"{n_views}views", f"FBP_{n_views}views",
              f"Img_CNN_{n_views}views", f"Sin_CNN_{n_views}views", "recon_64views"]:
        p = ROOT / "dataset" / dataset / "test" / d
        if p.exists():
            shutil.rmtree(p)

    print(">>> 步骤1: 数据预处理...")
    import subprocess
    ret = subprocess.run(
        ["python", "process-data.py",
         f"--dataset={dataset}", f"--n_views={n_views}",
         "--network=CNN", "--train=False"],
        cwd=str(ROOT), capture_output=True, text=True
    )
    if ret.returncode != 0:
        print(f"预处理失败: {ret.stderr}")
        sys.exit(1)
    print(ret.stdout)

    print(">>> 步骤2: 运行 LAMA 重建...")
    ret = subprocess.run(
        ["python", "demo-test.py",
         f"--dataset={dataset}", f"--n_views={n_views}", "--n_iter=3"],
        cwd=str(ROOT), capture_output=True, text=True
    )
    if ret.returncode != 0:
        print(f"推理失败: {ret.stderr}")
        sys.exit(1)
    print(ret.stdout)

    recon_file = ROOT / "dataset" / dataset / "test" / "recon_64views" / "data001.mat"
    if not recon_file.exists():
        print(f"Error: 重建结果未找到 {recon_file}")
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(str(recon_file), str(output_path))
    print(f">>> 步骤3: 重建完成，结果保存至 {output_path}")

    for line in ret.stdout.splitlines():
        if "avg PSNR" in line or "avg SSIM" in line:
            print(line)

if __name__ == "__main__":
    main()
