from pagamento import Pagamento

class PagamentoOffline(Pagamento):
    def realizarPagamento(pagamentoTipo: str):
        if pagamentoTipo == "pix":
            return "Pagemento Pix de forma offline realizado"
        elif pagamentoTipo == "cartao":
            return "Pagemento Cartao de forma offline realizado"
        elif pagamentoTipo == "boleto":
            return "Pagemento Boleto de forma offline realizado"
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoTipo}")