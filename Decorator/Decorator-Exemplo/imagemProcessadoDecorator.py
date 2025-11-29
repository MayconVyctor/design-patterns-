from abc import abstractmethod
from processadorImagem import ProcessadorImagem

class ImageProcessorDecorator(ProcessadorImagem):
    def __init__(self, processadorImagem: ProcessadorImagem) -> None:
        self._processadorIMG = processadorImagem

    @abstractmethod
    def process(self, imagem: str) -> str:
        pass