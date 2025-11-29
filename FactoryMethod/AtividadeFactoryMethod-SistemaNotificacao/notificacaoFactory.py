from abc import ABC, abstractmethod
from notificacao import Notificacao

# Minha fabrica abstrata para criação de notificações.

class NotificacaoFactory(ABC):
    @abstractmethod
    def criarNotificacao(self, destino, mensagem) -> Notificacao:
        pass