from pagamento import Pagamento

class PagamentoOnlinePix(Pagamento):
    def efetuarPagamento(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Enviando PIX para valor de R$ {valor:.2f}.")