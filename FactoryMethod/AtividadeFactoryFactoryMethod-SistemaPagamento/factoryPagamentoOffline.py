from pagamentoFactory import PagamentoFactory
from pagamentoPix import PagamentoPix
from pagamentoCartao import PagamentoCartao
from pagamentoBoleto import PagamentoBoleto

class FactoryPagamentoOffline(PagamentoFactory):
    def criarPagamento(self, tipoPagamento: str):
        if tipoPagamento == "pix":
            return PagamentoPix()
        elif tipoPagamento == "cartao":
            return PagamentoCartao()
        elif tipoPagamento == "boleto":
            return PagamentoBoleto()
        else:
            raise ValueError("Tipo de pagamento inválido")