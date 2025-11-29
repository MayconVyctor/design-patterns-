from Observer.passaro import SujeitoPassaro
from Observer.pessoa import Pessoa

if __name__ == "__main__":
    pessoa1 = Pessoa ("Mike")
    pessoa2 = Pessoa ("Daniel")
    pessoa3 = Pessoa ("Livia")

    observavel = SujeitoPassaro("Canario da Terra")
    observavel.adicionarobservdor(pessoa1)
    observavel.adicionarobservdor(pessoa2)
    observavel.adicionarobservdor(pessoa3)

    observavel.notificarObservadores("Passaro Voou")
    observavel.notificarObservadores("Passaro Pousou")

    observavel.removerobservador(pessoa2)
    observavel.notificarObservadores("Passaro Morreu")