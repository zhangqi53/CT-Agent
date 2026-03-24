import torch
import numpy as np
import os
from src.DADiff import UnetRes, ResidualDiffusion

# 1. 强制设定参数 (模拟原代码逻辑)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
image_size = 512
num_unet = 1
objective = 'pred_res'
test_res_or_noise = "res"
condition = True
input_condition = False
input_condition_mask = False
sum_scale = 0.01

print(f"Loading model on {device}...")

# 2. 实例化模型 (一模一样的参数)
model = UnetRes(
    dim=64,
    dim_mults=(1, 2, 4, 8),
    num_unet=num_unet,
    condition=condition,
    input_condition=input_condition,
    objective=objective,
    test_res_or_noise = test_res_or_noise
)

diffusion = ResidualDiffusion(
    model,
    image_size=image_size,
    timesteps=1000,
    sampling_timesteps=2, # 为了快，先设成2步看看能不能跑通
    objective=objective,
    loss_type='l2',
    condition=condition,
    sum_scale=sum_scale,
    input_condition=input_condition,
    input_condition_mask=input_condition_mask,
    test_res_or_noise = test_res_or_noise
).to(device)

# 3. 加载权重
checkpoint_path = '/app/FoundDiff/checkpoints/FoundDiff/sample/model-400.pt'

if not os.path.exists(checkpoint_path):
    print(f"Error: Checkpoint file not found at {checkpoint_path}")
    print("让我们看看 checkpoints/FoundDiff 目录下到底有什么：")
    os.system('ls -lh /app/FoundDiff/checkpoints/FoundDiff/')
    exit(1)

print(f"Loading diffusion weights from {checkpoint_path}...")
data = torch.load(checkpoint_path, map_location=device)

if 'model' in data:
    diffusion.load_state_dict(data['model'])
else:
    diffusion.load_state_dict(data)
    
print("Diffusion Model loaded successfully!")

# 4. 读取你的测试图片
input_npy_path = '/data/zhchen/test_image.npy'
if not os.path.exists(input_npy_path):
    # 如果找不到，就临时随机生成一张 512x512 的假图来测试网络
    print(f"Input not found, generating random noise...")
    img_np = np.random.rand(512, 512).astype(np.float32)
else:
    print(f"Loading input image from {input_npy_path}...")
    img_np = np.load(input_npy_path)
    # 确保尺寸是 512x512
    if img_np.shape != (512, 512):
        print("Warning: resizing image to 512x512...")
        import cv2
        img_np = cv2.resize(img_np, (512, 512))

# 转换成 tensor (Batch, Channels, Height, Width)
# 假设是单通道灰度图
img_tensor = torch.from_numpy(img_np).unsqueeze(0).unsqueeze(0).to(device)

print(f"Input shape: {img_tensor.shape}")

# 5. 执行推理
print("Starting inference...")
with torch.no_grad():
    # 原代码的 sample 逻辑通常需要 condition (原图) 和 noise (初始噪声，如果没提供它会自己生成)
    # 这里我们直接调用它的 sample 方法。
    # 注意：由于 DADiff 的具体输入结构可能比较复杂（可能需要特定的字典格式），
    # 如果这里报错，我们需要根据实际情况微调输入格式。
    output = diffusion.sample(batch_size=1, x_input=[img_tensor])

print(f"Inference done! Output shape: {output.shape}")

# 6. 保存结果
out_np = output.cpu().squeeze().numpy()
np.save('/data/zhchen/output_image.npy', out_np)
print("Result saved to /data/zhchen/output_image.npy")