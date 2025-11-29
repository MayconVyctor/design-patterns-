from servicoPagamento import PagamentoOnOffFactory

class PagamentoOnline(PagamentoOnOffFactory):
    def realizarPagamentoOnline(pagamentoTipo: str):
        if pagamentoTipo == "pix":
            return "Pagamento Pix de forma online realizado"
        elif pagamentoTipo == "cartao":
            return "Pagamento Cartao de forma online realizado"
        elif pagamentoTipo == "boleto":
            return "Pagamento Boleto de forma online realizado"
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoTipo}")