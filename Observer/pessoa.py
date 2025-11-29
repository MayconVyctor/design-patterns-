from observador import Observador

class Pessoa(Observador):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, mensagem: str) -> None:
        print(f"{self.nome} Recebeu a Mensagem: {mensagem}")
