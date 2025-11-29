from notificacaoFactory import NotificacaoFactory
from notificacao import Notificacao
from notificacaoEmail import NotificacaoEmail

# Minha Fábrica concreta para notificações que nao sao urgentes
# Implementa uma estrategia mais normal usando o email como canal padrao


class FactoryNotificacaoNormal(NotificacaoFactory):

    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        return NotificacaoEmail(destino, mensagem)