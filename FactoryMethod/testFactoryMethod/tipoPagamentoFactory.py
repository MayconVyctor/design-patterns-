from pagamentoFactory import PagamentoFactory
from pagamentoOnline import PagamentoOnline
from pagamentoOffline import PagamentoOffline


class TipoDePagamentoFactory(PagamentoFactory):
    def criarPagamentoOnline(self):
      return PagamentoOnline()

    def criarPagamentoOffline(self):
        return PagamentoOffline()


