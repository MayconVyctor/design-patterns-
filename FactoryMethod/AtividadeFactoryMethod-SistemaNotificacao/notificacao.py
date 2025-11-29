from abc import ABC, abstractmethod

# Minha Classe abstrata base para todos os tipos de notificação.
#Define a interface comum que todas as notificações concretas devem implementar

class Notificacao(ABC):

    def __init__(self, destino: str, mensagem: str) -> None:
        self.destino = destino
        self.mensagem = mensagem

    @abstractmethod
    def enviarNotificacao(self):
       # Metodo abstrato que sera implementado pelas subclasses
        pass

