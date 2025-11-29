
from factoryPagamentoOnline import FactoryPagamentoOnline
from factoryPagamentoOffline import FactoryPagamentoOffline

# Cliente usa fábrica ONLINE
factoryOnline = FactoryPagamentoOnline()
clientePagamento1 = factoryOnline.criarPagamento("pix")
print(clientePagamento1.realizarPagamento())

clientePagamento2 = factoryOnline.criarPagamento("cartao")
print(clientePagamento2.realizarPagamento())

# Cliente usa fábrica OFFLINE
factoryOffline = FactoryPagamentoOffline()
pagamento3 = factoryOffline.criarPagamento("boleto")
print(pagamento3.realizarPagamento())


"""
Atividade - Padrões Simple Factory e Factory Method

Objetivo:
Aplicar os padrões de projeto Simple Factory e Factory Method para desacoplar a
criação de objetos de sua utilização, promovendo flexibilidade e extensibilidade.
Descrição da Tarefa:
Desenvolva duas partes (ou dois módulos) do sistema, cada uma usando uma versão do
padrão Simple Factory e Factory Method:


1. Sistema de Pagamento
● Crie uma hierarquia de classes para representar diferentes formas de pagamento:
por exemplo, Pagamento (classe abstrata ou interface), e classes concretas como
PagamentoCartao, PagamentoBoleto, PagamentoPix.

● Crie também uma fábrica abstrata (PagamentoFactory) que define um método
criarPagamento(...).

● Implemente dois criadores concretos (subclasses de PagamentoFactory), por
exemplo FactoryPagamentoOnline e FactoryPagamentoOffline, que
decidem, com base em algum parâmetro, qual tipo de pagamento criar.

● No cliente (por exemplo, uma função ou classe de serviço), use a fábrica para obter
instâncias de Pagamento, sem depender diretamente das classes concretas.


"""
