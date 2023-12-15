from __future__ import annotations
from typing import Final as const, Any

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import json

from DXSuite.API import DXSuiteAPI, load_auth_data

app = FastAPI()

@app.post('/easyocr')
async def read_ocr(file: UploadFile = File(...)):
    """_summary_
    EasyOCRを用いて画像からOCRを行うエンドポインt
    Args:
        file (UploadFile): 画像ファイル
    Returns:
        OCR結果
    """
    # 画像をバイナリ形式に変換
    img = await file.read()
    # OCRを行う
    result = DXSuiteAPI().read(img)
    return result

if __name__ == "__main__":
    # JSONファイルから設定を読み込む
    with open("config.json", "r") as f:
        config = json.load(f)
    
    port = config.get("port", 8000)  # 指定がなければ8000番ポートを使用

    # uvicornをプログラムから起動
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


