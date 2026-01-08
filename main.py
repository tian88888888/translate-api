from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dotenv import load_dotenv
from openai import OpenAI
import os, json


load_dotenv()
app = FastAPI()


DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise RuntimeError("DEEPSEEK_API_KEY未设置")

client = OpenAI(
    api_key = DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)
class TranslateRequest(BaseModel):
    text: str

@app.post("/translate")
def translate(req: TranslateRequest): 
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="text不能为空")

    prompt = f"""
请完成两件事：
1. 把下面的中文翻译成英文
2. 提取三个英文关键词
输出JSON格式如下：
{{
  "translation": "...",
  "keywords": ["...", "...", "..."]
}}
翻译的中文内容：
{req.text}
""".strip()
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        result_text = response.choices[0].message.content.strip()

        result_json = json.loads(result_text)

        return {
            "translation": result_json["translation"],
            "keywords": result_json["keywords"]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
