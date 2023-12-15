import easyocr
from easyocr.easyocr import Reader
from numpy import ndarray


from ..AbsOCRAPI import AbsOCR
from Interface import EastOCRParam, OCRResult



class EasyOCRReader(AbsOCR):

    def __init__(self, param: EastOCRParam):

        self.reader = Reader(**param.model_dump())


    def read(self, img:str | ndarray | bytes) -> OCRResult:

        return self.reader.readtext(img)





