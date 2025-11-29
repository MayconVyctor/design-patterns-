from processadorImagem import ProcessadorImagem

class BasicoImageProcessor(ProcessadorImagem):
    def process(self, imagem: str) -> str:
        novaImagem = "/uploads/file_processed.jpg"
        # TODO: Implement the basic image processing logic
        print(f"Processa a imagem de {imagem} para {novaImagem}")

        return novaImagem