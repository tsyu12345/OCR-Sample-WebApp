from abc import ABC
from abc import abstractmethod
from pydantic import BaseModel

from PIL import Image



class AbsOCR(ABC):
    """_summary_
    OCR APIの抽象クラス
    """

    def __init__(self, Param: BaseModel):
        pass

    @abstractmethod
    def read(self, img) -> None:
        """
        画像からOCRを行い、結果を返す
        Args:
            img (Image): 入力画像
        """
        pass
