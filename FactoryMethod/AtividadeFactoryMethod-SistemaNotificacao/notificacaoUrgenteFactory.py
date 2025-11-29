from notificacaoFactory import NotificacaoFactory
from notificacao import Notificacao
from notificacaoWhatsApp import NotificacaoWhatsApp
from notificacaoSMS import  NotificacaoSMS

# Minha fabrica concreta para notificações urgentes (mais especificamente as de whastapp).
# Implementei de uma forma que essas notificacoes priorizem o whatsapp atravez de uma verificação se
# o numero de contato informado for igual a 14 que seria '+5533984638281' ele é classificado como numero de whatsapp
# e se for igual a 11 cai como SMS

class FactoryNotificacaoUrgente(NotificacaoFactory):
    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        if len(destino) == 11:
            return NotificacaoSMS(destino, mensagem)
        elif len(destino) == 14:
            return NotificacaoWhatsApp(destino, mensagem)
        else:
            return NotificacaoSMS(destino, mensagem)
