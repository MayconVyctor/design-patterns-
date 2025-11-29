from notificacao import Notificacao

class NotificacaoEmail(Notificacao):
    def enviarNotificacao(self):
        print(f"[EMAIL] Enviando para {self.destino}: '{self.mensagem}'")

# Classe que Herda de Notificacao.
# Implementa enviarNotificacao()
# Simula envio com print()