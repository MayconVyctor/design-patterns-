from pagamentoFactory import PagamentoFactory

def realizarPagamento(tipo: str, forma: str, valor: float):
    pagamentoFactory = PagamentoFactory()
    pagamento = pagamentoFactory.criarPagamento(tipo, forma)
    pagamento.efetuarPagamento(valor)

if __name__ == "__main__":
    realizarPagamento("offline", "boleto", 1600.0)
    realizarPagamento("online", "cartao", 550.0)
    realizarPagamento("online", "pix", 50.0)
    realizarPagamento("offline", "cartao", 10.0)