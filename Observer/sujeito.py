from abc import ABC, abstractmethod
from observador import *


class Sujeito(ABC):
    @abstractmethod
    def adicionarobservdor(self, observador: Observador):
        pass

    @abstractmethod
    def removerobservador(self, observador: Observador):
        pass

    @abstractmethod
    def notificarObservadores(self, mensagem):
        pass

    # precisar desses tres tipos de metodo