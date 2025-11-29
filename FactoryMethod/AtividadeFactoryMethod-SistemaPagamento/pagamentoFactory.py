from abc import ABC, abstractmethod
from pagamento import Pagamento

class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, tipo: str) -> Pagamento:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass