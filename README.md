Translate API (FastAPI)

基于 FastAPI 构建的后端接口服务，调用大模型API，实现中文到英文翻译，并自动提取三个英文关键词

# 接口说明
- POST /translate
- 参数： {"text": “中文"}
- 返回结果： {"translation": "...", "keywords": ["...","...", "..."]}


# Setup
- Python 3.14
- FastAPI
- DeepSeek 大模型 API

# 本地运行
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

创建.env文件存储API Key

# 启动服务
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

访问接口文档（Swagger测试）：
http://127.0.0.1:8000/docs


