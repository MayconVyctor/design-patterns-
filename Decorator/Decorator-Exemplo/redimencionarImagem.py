from processadorImagem import ProcessadorImagem

class RedimencionarImagem(ProcessadorImagem):

        def __init__(self, imagem: ProcessadorImagem):
            self.imagem = imagem

        def processar(self, caminho):
            novaImagem = "redimencionada.jpg"
            imagem.processar(caminho)

