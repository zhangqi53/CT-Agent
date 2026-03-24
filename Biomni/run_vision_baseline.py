import os

# 1. 🚀 降维打击：在任何框架加载前，强行在内存中伪造 OpenAI 的环境变量！
os.environ["OPENAI_API_KEY"] = "sk-0d87f4d715a14eac938b49ce98fbae8d" # 👈 换成你的 Key
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com/v1" # 欺骗系统请求 DeepSeek
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com/v1" # 兼容新老版本的环境变量名

from biomni.agent import A1
from biomni.tool.tool_description.imaging_desc import evaluate_ct_quality_desc

# 2. 初始化 Agent，既然上面环境变量已经配好了，这里只需要指明模型名即可
agent = A1(
    llm="deepseek-chat",               
    source="OpenAI"                   
)

# 3. 绕过系统的自动扫描，强行把工具说明书注册进引擎
try:
    agent.tool_registry.register_tool(evaluate_ct_quality_desc)
    print("✅ PR-IQA 工具说明书强行注入成功！")
except Exception as e:
    print(f"⚠️ 注入失败，请检查: {e}")

# 4. 用大白话下发测试指令
prompt = """
我有一张 CT 重建图像，绝对路径是 /home/liuyiwei/cut_image/cut_lama/LAMA_data001.png。
请你调用 evaluate_ct_quality 工具，帮我测一下这张图的客观得分，并告诉我结果。
"""

print("🤖 Biomni Agent (DeepSeek全网通版) 正在思考并调用底层 Docker，请稍候...\n")

# 5. 让 Agent 开始执行任务
response = agent.go(prompt) 

# 6. 打印最终结果
print("\n================ 最终回复 ================")
print(response)