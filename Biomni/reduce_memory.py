import numpy as np
from scipy.ndimage import zoom
import shutil
import os

input_file = 'test_data/input/chest_data.npz'
backup_file = 'test_data/input/chest_data_512_backup.npz'

print("1. 正在备份原始高清数据...")
if not os.path.exists(backup_file):
    shutil.copy(input_file, backup_file)
    print(f"   备份已保存至: {backup_file}")
else:
    print("   备份文件已存在，跳过备份。")

print("\n2. 正在加载当前数据...")
data = np.load(input_file)['data']
print(f"   原始数据形状: {data.shape}")

print("\n3. 正在进行下采样 (80, 512, 512) -> (80, 256, 256)...")
print("   (这可能需要十几秒钟，请耐心等待)")
# 核心降维代码：Z轴保持1倍，长宽缩小0.5倍，使用线性插值(order=1)
small_data = zoom(data, (1, 0.5, 0.5), order=1)
print(f"   ✅ 降维后数据形状: {small_data.shape}")

print("\n4. 正在覆盖保存...")
np.savez(input_file, data=small_data.astype(np.float32)) # 顺便转为 float32 进一步省显存
print("   ✅ 显存友好版数据已就绪！")
