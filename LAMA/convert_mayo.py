# convert_mayo_v2.py
import numpy as np
import pydicom
import scipy.io as scio
import torch
import ctlib
from pathlib import Path
from tqdm import tqdm
import sys
sys.path.append('/app')
import utils.CT_helper as CT

DATA_ROOT = Path("/data")
SAVE_ROOT = Path("/app/dataset/mayo")
PATIENTS = ["C002", "C004"]
TRAIN_RATIO = 0.8

def read_ct_images(img_dir):
    """读取Full dose CT图像DICOM文件，返回归一化图像列表"""
    files = sorted(img_dir.glob("*.dcm"))
    images = []
    for f in files:
        ds = pydicom.dcmread(str(f), force=True)
        arr = ds.pixel_array.astype(np.float32)
        # HU值转换
        slope = float(getattr(ds, 'RescaleSlope', 1.0))
        intercept = float(getattr(ds, 'RescaleIntercept', -1024.0))
        arr = arr * slope + intercept
        # HU归一化到[0,1]，窗宽窗位 [-160, 240] HU
        arr = (arr - (-160)) / (240 - (-160))
        arr = arr.clip(0, 1)
        # resize到256x256
        import cv2
        arr = cv2.resize(arr, (256, 256))
        images.append(arr)
    return images

def main():
    ct_cfg = CT.load_CT_config('/app/config/full-view.yaml')
    mask = CT.generate_mask()
    
    all_sinos = []
    
    for patient in PATIENTS:
        patient_dir = DATA_ROOT / patient
        for scan_dir in sorted(patient_dir.iterdir()):
            for sub in sorted(scan_dir.iterdir()):
                if "full dose images" in sub.name.lower():
                    print(f"\nReading CT images from {sub} ...")
                    images = read_ct_images(sub)
                    print(f"  Got {len(images)} CT slices")
                    
                    # 每张CT图像生成一个正弦图
                    for img in tqdm(images, desc="Generating sinograms"):
                        img_tensor = torch.FloatTensor(img).reshape(1,1,256,256).cuda()
                        # 正向投影生成1024视角正弦图
                        sino = ctlib.projection(img_tensor, ct_cfg)
                        sino = sino.squeeze().detach().cpu().numpy()  # (1024, 512)
                        all_sinos.append(sino.astype(np.float32))
    
    print(f"\nTotal sinograms: {len(all_sinos)}")
    
    # 清空旧数据
    import shutil
    for split in ['train', 'test']:
        d = SAVE_ROOT / split / 'FullViewNoiseless'
        if d.exists():
            shutil.rmtree(d)
    
    # 打乱分割保存
    np.random.seed(42)
    idx = np.random.permutation(len(all_sinos))
    n_train = int(len(all_sinos) * TRAIN_RATIO)
    
    for split, indices in [("train", idx[:n_train]), ("test", idx[n_train:])]:
        save_dir = SAVE_ROOT / split / "FullViewNoiseless"
        save_dir.mkdir(parents=True, exist_ok=True)
        for i, j in enumerate(tqdm(indices, desc=f"Saving {split}")):
            scio.savemat(save_dir / f"data{i+1:03d}.mat", {"data": all_sinos[j]})
        print(f"Saved {len(indices)} {split} sinograms → {save_dir}")

if __name__ == "__main__":
    main()