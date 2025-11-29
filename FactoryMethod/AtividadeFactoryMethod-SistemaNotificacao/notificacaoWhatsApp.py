from notificacao import Notificacao

class NotificacaoWhatsApp(Notificacao):
    def enviarNotificacao(self):
        print(f"[WHATSAPP] Enviando para {self.destino}: '{self.mensagem}'")


# Classe que Herda de Notificacao.
# Implementa enviarNotificacao()
# Simula envio com print()