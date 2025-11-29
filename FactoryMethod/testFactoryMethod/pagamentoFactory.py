from abc import ABC, abstractmethod
from pagamento import Pagamento


# Creator abstrato - Factory Method Pattern
class PagamentoFactory(ABC):

    @abstractmethod
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass
