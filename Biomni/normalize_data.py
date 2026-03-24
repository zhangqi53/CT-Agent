import numpy as np

input_file = 'test_data/input/chest_data.npz'
data = np.load(input_file)['data']

print(f"处理前数据最大值: {data.max()}")

if data.max() > 1.0:
    print("正在进行归一化处理...")
    # 核心步骤：强制除以最大值
    data = data.astype(np.float32) / data.max()
    np.savez(input_file, data=data)
    print(f"✅ 归一化完成！当前最大值: {data.max()} (应该是 1.0)")
else:
    print("✅ 数据已经是归一化状态。")
