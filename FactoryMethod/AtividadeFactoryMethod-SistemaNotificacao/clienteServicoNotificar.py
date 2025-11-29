from notificacaoFactory import  NotificacaoFactory

# A classe cliente depende apenas da interface abstrata `NotificacaoFactory`,
# não das implementações concretas e com isso conseguimos trocar as estratégias urgente/nao urgente)
# sem modificar o código

class ClienteServicoNotificar:
    def __init__(self, factory: NotificacaoFactory) -> None:
        self.factory = factory

    def enviarNotificacao(self, destino: str, mensagem: str) -> None:

        notificacao = self.factory.criarNotificacao(destino, mensagem)
        notificacao.enviarNotificacao()