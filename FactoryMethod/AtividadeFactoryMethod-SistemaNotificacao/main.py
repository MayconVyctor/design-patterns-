

'''''
2. Sistema de Notificação
● Crie uma hierarquia para notificações: classe base Notificacao, e subclasses
como c, NotificacaoSMS, NotificacaoWhatsApp.
● Crie uma fábrica abstrata NotificacaoFactory, com método
criarNotificacao(destino, mensagem) (ou parâmetros que você achar
relevante).
● Implemente duas fábricas concretas, por exemplo FactoryNotificacaoUrgente
(que pode priorizar SMS ou WhatsApp) e FactoryNotificacaoNormal (que pode
usar e-mail ou outro canal).
● Crie um cliente (serviço de notificação) que usa a fábrica para gerar uma
Notificacao apropriada e enviá-la (você pode simular o envio com print() se
quiser).
Requisitos Técnicos:
1. Utilize herança e polimorfismo para definir a estrutura (“Product” abstrato, “Creators”
concretos), conforme o padrão Factory Method clássico.
2. Use abc.ABC e @abstractmethod para definir as classes abstratas, se desejar,
para reforçar o contrato.
3. Documente bem cada classe e método com docstrings, explicando o que cada parte
faz.
4. Escreva um pequeno script main demonstrando:
○ No sistema de pagamento: criação de diferentes tipos de pagamento por
meio da fábrica e execução de alguma operação (ex: pagar()).
○ No sistema de notificação: criação de notificações diferentes por meio da
fábrica e “envio” da mensagem.
'''

from notificacaoUrgenteFactory import FactoryNotificacaoUrgente
from notificacaoNaoUrgente import FactoryNotificacaoNormal
from clienteServicoNotificar import ClienteServicoNotificar

# Este é o meu Script de demonstração do sistema de notificação.
#    Ele Mostra:
#     - Criação de notificações urgentes (WhatsApp/SMS) via FactoryNotificacaoUrgente.
#     - Criação de notificações normais (e-mail) via FactoryNotificacaoNormal.
#     - Desacoplamento total entre cliente e produtos concretos.

if __name__ == "__main__":
    print("Sistema de Notificação")
    factoryUrgente = FactoryNotificacaoUrgente()
    factoryNaoUrgente = FactoryNotificacaoNormal

    # Notificação urgente
    print("Urgente:")
    clienteServicoUrgente = ClienteServicoNotificar(FactoryNotificacaoUrgente())
    clienteServicoUrgente.enviarNotificacao("+5577999999999", "Pedido a caminho!")
    clienteServicoUrgente.enviarNotificacao("33984638281", "Alerta!")  # vai para SMS (fallback)

    # Notificação normal
    print("Nao Urgente/Normal:")
    clienteServicoNaoUrgente = ClienteServicoNotificar(FactoryNotificacaoNormal())
    clienteServicoNaoUrgente.enviarNotificacao("maycon@ifba.edu.br", "Boleto disponível.")



