from processadorImagem import ProcessadorImagem
class MarcaDagua(ProcessadorImagem):
    def __init__(self, imagem: ProcessadorImagem):
        self.imagem = imagem

    def processar(self, caminho):
        novaImagem = "marcaDagua.jpg"
        imagemRecebida = imagem.processar(caminho)
        print(f"Transforma {imagemRecebida} para com {marcaDagua}")
        print(f"de {caminho} para {caminhio}")
