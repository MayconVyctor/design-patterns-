from notificacao import Notificacao

class NotificacaoSMS(Notificacao):
    def enviarNotificacao(self):
        print(f"[SMS] Enviando para {self.destino}: '{self.mensagem}'")


# Classe que Herda de Notificacao.
# Implementa enviarNotificacao()
# Simula envio com print()