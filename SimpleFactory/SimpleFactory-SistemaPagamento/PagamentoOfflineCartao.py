from pagamento import Pagamento

class PagamentoOfflineCartao(Pagamento):
    def efetuarPagamento(self, valor: float):
        print(f"Pagamento Offline.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")