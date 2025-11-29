from abc import ABC, abstractmethod

class ProcessadorImagem(ABC):
    @abstractmethod
    def procesar(self, imagem: str) -> str:
        pass