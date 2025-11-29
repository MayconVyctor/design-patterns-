from pagamentoBoletoFactory import  PagamentoBoletoFactory
from pagamentoCartaoFactory import PagamentoCartaoFactory
from pagamentoPixFactory import PagamentoPixFactory
from tipoPagamentoFactory import TipoDePagamentoFactory

#tipoDePagamentoFactory = TipoDePagamentoFactory()

pagamentoPix1 = PagamentoPixFactory.criarPagamento("pix")
print(pagamentoPix1.realizarPagamento())
pagamentoPix1 = TipoDePagamentoFactory.criarPagamentoOnline("cartao")
print(pagamentoPix1.realizarPagamentoOnline("cartao"))

#pagamentoCartao1 = PagamentoCartaoFactory.criarPagamento("cartao")
#print(pagamentoCartao1.realizarPagamento())

#pagamentoBoleto1 = PagamentoBoletoFactory.criarPagamento("boleto")
#print(pagamentoBoleto1.realizarPagamento())



