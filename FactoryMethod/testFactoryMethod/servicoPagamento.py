from abc import ABC, abstractmethod


# Creator abstrato - Factory Method Pattern
class PagamentoOnOffFactory(ABC):
    @abstractmethod
    def realizarPagamentoOnline(pagamentoTipo: str):
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass