import os

# 1. 🚀 降维打击：在任何框架加载前，强行在内存中伪造 OpenAI 的环境变量！
os.environ["OPENAI_API_KEY"] = "sk-0d87f4d715a14eac938b49ce98fbae8d" # 👈 你的 Key
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com/v1" 
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com/v1" 

from biomni.agent import A1
from biomni.tool.tool_description.imaging_desc import evaluate_ct_quality_desc

# 2. 初始化 Agent
agent = A1(
    llm="deepseek-chat",               
    source="OpenAI"                   
)

# 3. 强行把工具说明书注册进引擎
try:
    agent.tool_registry.register_tool(evaluate_ct_quality_desc)
    print("✅ 批量版 PR-IQA 工具说明书强行注入成功！")
except Exception as e:
    print(f"⚠️ 注入失败，请检查: {e}")

# 4. 用大白话下发测试指令 (⚠️ 这里改成了批量评估的指令)
prompt = """
[最高系统指令 - 强制执行]
你现在的唯一任务是评估 152 张 CT 影像。请你严格遵循以下要求：
1. 必须且只能调用 `evaluate_ct_quality` 工具（不需要传参）来触发后台 Docker 运行！
2. 绝对禁止你自己编写 Python 代码去硬盘上搜索或读取任何现成的 .mat、.csv 或 .json 文件！我要的是重新运行得出的最新结果。
3. 请直接等待 `evaluate_ct_quality` 工具返回最终的 JSON 结果。
4. 拿到结果后，告诉我：平均融合分是多少？排名前五的影像是哪几张，分数分别是多少？？
"""

print("🤖 Biomni Agent (DeepSeek全网通版) 正在思考并调用底层 Docker 跑 152 张图，请耐心等待...\n")

# 5. 让 Agent 开始执行任务
response = agent.go(prompt) 

# 6. 打印最终结果
print("\n================ 最终回复 ================")
print(response)