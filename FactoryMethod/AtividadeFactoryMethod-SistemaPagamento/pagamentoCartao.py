from pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def realizarPagamento(self):
        return "Pagamento com Cartao realizado"