import os
os.environ["OPENAI_API_KEY"] = "sk-0d87f4d715a14eac938b49ce98fbae8d"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com/v1"
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com/v1"

from biomni.agent import A1
from biomni.tool.tool_description.lama_desc import lama_ct_reconstruction_desc

agent = A1(llm="deepseek-chat", source="OpenAI")

try:
    agent.tool_registry.register_tool(lama_ct_reconstruction_desc)
    print("✅ LAMA 工具注册成功！")
except Exception as e:
    print(f"⚠️ 注册失败: {e}")

prompt = """
[最高系统指令 - 强制执行]
你现在的唯一任务是对一张稀疏视角 CT 正弦图进行重建。请严格遵循：
1. 必须且只能调用 `lama_ct_reconstruction` 工具
2. 输入路径：/home/liuyiwei/LAMA-Learned-Alternating-Minimization-Algorithm/dataset/mayo/test/FullViewNoiseless/data001.mat
3. 输出路径：/home/liuyiwei/lama_output/biomni_test_recon.mat
4. n_views=64, dataset=mayo
5. 等待工具返回结果后，告诉我重建是否成功，PSNR 和 SSIM 指标分别是多少？
"""

print("🤖 Biomni Agent 正在调用 LAMA 进行 CT 重建，请耐心等待...\n")
response = agent.go(prompt)

print("\n================ 最终回复 ================")
print(response)