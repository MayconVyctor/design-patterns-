from pagamentoFactory import PagamentoFactory
from pagamentoPix import PagamentoPix

class PagamentoPixFactory(PagamentoFactory):
    def criarPagamento(self):
        return PagamentoPix()