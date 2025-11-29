from pagamentoFactory import PagamentoFactory
from pagamentoBoleto import PagamentoBoleto

class PagamentoBoletoFactory(PagamentoFactory):
    def criarPagamento(self):
        return PagamentoBoleto()