from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def efetuarPagamento(self, valor: float):
        pass