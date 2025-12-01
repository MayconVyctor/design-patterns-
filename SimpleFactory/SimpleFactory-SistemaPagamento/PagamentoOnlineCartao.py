from pagamento import Pagamento

class PagamentoOnlineCartao(Pagamento):
    def efetuarPagamento(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")