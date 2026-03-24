import json
import os
from google import genai
from PIL import Image

# 1. 初始化新版客户端 (只要你 export 了 GEMINI_API_KEY，它会自动读取)
client = genai.Client()

# 2. 定义系统提示词：加入组图说明
SYSTEM_PROMPT = """
你是一名资深放射科医生。我提供给你的CT图像是一组由 6 张连续切片横向拼接而成的组图。
请综合观察这些切片，严格按照以下四级结构输出诊断报告：
1. 特征提取（客观描述病灶形态、大小、密度、边缘等特征）
2. 病灶定位（精确到具体的解剖结构）
3. 良恶性概率（基于影像特征给出良恶性的倾向性判断）
4. 临床建议（提供具体、可操作的下一步诊疗建议）
注意：不要输出多余的解释，直接输出这四点内容。
"""

# 3. 核心调用函数
def run_vision_baseline(image_path):
    img = Image.open(image_path)
    prompt = "请根据这张CT拼接组图出具四级结构诊断报告。"
    
    # 使用新版 API 的调用方式
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[prompt, img],
        config=genai.types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.1
        )
    )
    return response.text

# 4. 主执行逻辑
def main():
    # 读取数据集
    with open('vision_dataset.json', 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    results = []
    
    for case in dataset:
        print(f"正在处理图像: {case['image_path']} ...")
        
        # 检查图片是否存在
        if not os.path.exists(case['image_path']):
            print(f"❌ 找不到图片: {case['image_path']}，请检查文件名和路径。")
            continue
            
        # 调用大模型
        try:
            output = run_vision_baseline(case['image_path'])
            print("✅ 处理成功！输出内容如下：\n", output)
        except Exception as e:
            print(f"❌ 调用 API 失败: {e}")
            output = f"Error: {e}"
        
        # 记录结果
        results.append({
            "id": case["id"],
            "image_path": case["image_path"],
            "vlm_output": output,
            "ground_truth": case["ground_truth"]
        })
    
    # 将结果保存到 results 文件夹中
    output_path = os.path.join('results', 'vision_baseline_results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n🎉 视觉基线跑通！结果已保存至: {output_path}")

if __name__ == "__main__":
    main()