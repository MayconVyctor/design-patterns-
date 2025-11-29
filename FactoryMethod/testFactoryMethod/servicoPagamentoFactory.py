from abc import ABC, abstractmethod


# Creator abstrato - Factory Method Pattern
class servicoPagamentoFactory(ABC):

     @abstractmethod
     def criarPagamentoOnline(self):
         pass