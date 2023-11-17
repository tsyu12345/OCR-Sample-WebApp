from abc import ABCMeta
from abc import abstractmethod
from pydantic import BaseModel

from PIL import Image



class AbsOCRAPI(metaclass = ABCMeta):
    """_summary_
    OCR APIの抽象クラス
    """

    def __init__(self,):
        pass

    @abstractmethod
    def read_img(self, img) -> None:
        """
        画像からOCRを行い、結果を返す
        Args:
            img (Image): 入力画像
        """
        pass
