from abc import ABC, abstractmethod

class ProcessadorImagem(ABC):
    @abstractmethod
    def procesar(self, caminho):
        pass