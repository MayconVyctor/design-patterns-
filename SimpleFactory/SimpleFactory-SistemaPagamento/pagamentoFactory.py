from pagamento import Pagamento
from PagamentoOnlineCartao import PagamentoOnlineCartao
from PagamentoOfflineCartao import PagamentoOfflineCartao
from PagamentoOfflineBoleto import PagamentoOfflineBoleto
from PagamentoOnlinePix import PagamentoOnlinePix

class PagamentoFactory:

    def criarPagamento(self, tipo: str, forma: str) -> Pagamento:
        tipo = tipo.lower()
        forma = forma.lower()
        if tipo == "online":
            if forma == "cartao":
                return PagamentoOnlineCartao()
            elif forma == "pix":
                return PagamentoOnlinePix()
            else:
                raise ValueError(f"Forma de pagamento online não suportada: {forma}")

        elif tipo == "offline":
            if forma == "cartao":
                return PagamentoOfflineCartao()
            elif forma == "boleto":
                return PagamentoOfflineBoleto()
            else:
                raise ValueError(f"Forma de pagamento offline não suportada: {forma}")

        else:
            raise ValueError(f"Tipo de pagamento não suportado: '{tipo}'")
