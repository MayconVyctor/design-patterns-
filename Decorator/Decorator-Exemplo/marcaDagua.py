from processadorImagem import ProcessadorImagem
class MarcaDagua(ProcessadorImagem):
    ##def __init__(self, imagemPathProcessadorImagem):
    #    self.imagemPath = imagemPath

    def processar(self, imagem: str) -> str:
        imagemProcessada = self._processadorIMG("marcaDagua.jpg")
        novaImagem = "/uploads/marcaDagua_file.jpg"
        print(f"Processa a imagem de {imagemProcessada} para {novaImagem}")
        return novaImagem
