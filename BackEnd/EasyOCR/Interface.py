from typing import Final as const, Any, Optional
from pydantic import BaseModel


class EastOCRParam(BaseModel):
    lang_list: list[str]
    gpu: bool = True
    model_storage_directory: Optional[str] = None
    user_network_directory: Optional[str] = None
    detect_network: str = "craft"
    recog_network: str = 'standard'
    download_enabled: bool = True
    detector: bool = True
    recognizer: bool = True
    verbose: bool = True
    quantize: bool = True
    cudnn_benchmark: bool = False


class OCRResult(BaseModel):
    points: tuple[list[list[int]]]
    text: str
    confidence: float 