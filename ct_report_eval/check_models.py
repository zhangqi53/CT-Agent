from google import genai

# 初始化客户端（会自动读取你刚才 export 的 GEMINI_API_KEY）
client = genai.Client()

print("你的 API Key 目前支持以下模型：\n")
# 获取并打印所有可用的模型名称
for model in client.models.list():
    print(model.name)