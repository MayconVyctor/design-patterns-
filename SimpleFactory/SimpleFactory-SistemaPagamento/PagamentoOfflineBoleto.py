from pagamento import Pagamento

class PagamentoOfflineBoleto(Pagamento):
    def efetuarPagamento(self, valor):
        print(f"Pagamento Offline.",end=" ")
        print(f"Gerando boleto para R$ {valor:.2f}.")