from pagamentoFactory import PagamentoFactory
from pagamentoCartao import PagamentoCartao

class PagamentoCartaoFactory(PagamentoFactory):
    def criarPagamento(self):
        return PagamentoCartao()