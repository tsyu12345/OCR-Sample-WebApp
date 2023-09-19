from __future__ import annotations
from typing import Final as const, Any

from fastapi import FastAPI
import uvicorn
import json

from DXSuite.API import DXSuiteAPI, load_auth_data


app = FastAPI()

@app.get("/")
def read_root():
    return {"test": "HelloWorld"}


if __name__ == "__main__":
    # JSONファイルから設定を読み込む
    with open("config.json", "r") as f:
        config = json.load(f)
    
    port = config.get("port", 8000)  # 指定がなければ8000番ポートを使用

    # uvicornをプログラムから起動
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


