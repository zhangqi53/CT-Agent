import argparse
import json
import sys
import os
import torch
from torchvision import transforms
from PIL import Image

# 依赖同级目录机制，直接导入官方核心代码
try:
    from eagle_loss import EagleLoss
except ImportError as e:
    print(json.dumps({"status": "error", "message": f"导入官方模块失败，请检查目录层级。详情: {e}"}))
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Eagle-Loss Tool for Biomni")
    parser.add_argument("--recon", required=True, help="重建 CT 图像的绝对路径")
    parser.add_argument("--gt", required=True, help="Ground Truth CT 图像的绝对路径")
    parser.add_argument("--kappa", type=float, default=0.6, help="高斯滤波器的截止频率")
    parser.add_argument("--patch_size", type=int, default=3, help="方差计算块大小")
    
    args = parser.parse_args()

    try:
        # 1. 验证文件路径
        if not os.path.exists(args.recon) or not os.path.exists(args.gt):
            raise FileNotFoundError("找不到指定的图像文件，请检查挂载路径。")

        # 2. 预处理：灰度转换与张量化 (1, 1, H, W)
        transform = transforms.Compose([transforms.Grayscale(), transforms.ToTensor()])
        I_rec = transform(Image.open(args.recon)).unsqueeze(0)
        I_g = transform(Image.open(args.gt)).unsqueeze(0)

        if I_rec.shape != I_g.shape:
            raise ValueError(f"尺寸不匹配: Recon 为 {I_rec.shape}，GT 为 {I_g.shape}")

        # 3. 分配硬件设备
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        I_rec = I_rec.to(device)
        I_g = I_g.to(device)

        # 4. 实例化官方模型并计算 Loss
        criterion = EagleLoss(patch_size=args.patch_size, kappa=args.kappa).to(device)
        criterion.eval()
        with torch.no_grad():
            loss_val = criterion(I_rec, I_g).item()
        
        # 5. 成功执行，仅输出 JSON
        result = {
            "status": "success",
            "eagle_loss": round(loss_val, 6),
            "parameters": {
                "kappa": args.kappa,
                "patch_size": args.patch_size
            },
            "device": str(device)
        }
        print(json.dumps(result))
        sys.exit(0)
        
    except Exception as e:
        # 6. 异常捕获，输出错误信息的 JSON
        error_result = {
            "status": "error",
            "message": str(e)
        }
        print(json.dumps(error_result))
        sys.exit(1)

if __name__ == "__main__":
    main()