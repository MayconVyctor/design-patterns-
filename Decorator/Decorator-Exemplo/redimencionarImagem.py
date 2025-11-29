from processadorImagem import ProcessadorImagem

class RedimencionarImagem(ProcessadorImagem):

       # def __init__(self, imagem: ProcessadorImagem):
        #    self.imagem = imagem

        def processar(self, imagem: str) -> str:
            imagemProcessada= self._processarIMG.processar("redimencionada.jpg")
            # TODO: Implementa a lógica do redimensionamento
            novaImagem = "/uploads/resized_file.jpg"
            print(f"Processa a imagem de {imagemProcessada} para {novaImagem}")
            return novaImagem

