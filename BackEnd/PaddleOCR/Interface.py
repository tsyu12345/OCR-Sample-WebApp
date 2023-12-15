from pydantic import BaseModel

class PaddleOCRParam(BaseModel):
    user_gpu: bool = False
    lang: str = "japan"
    max_text_length: int
