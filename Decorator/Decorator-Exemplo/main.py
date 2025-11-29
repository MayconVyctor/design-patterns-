from basicoProcessadorImagen import BasicoImageProcessor
from marcaDagua import MarcaDagua
from redimencionarImagem import RedimencionarImagem

print("=== Teste do Padrão Decorator ===\n")

if __name__ == "__main__":
    imagem = "/temp/file.jpg"

    # composicao 0
    print(" Composicao 0: basico")
    imagemProcessar = RedimencionarImagem(BasicoImageProcessor())
    imagemProcessar.process(imagem)

    # Composicao 1
    print("\n\nComposicao 1:")
    imageProcessor = BasicoImageProcessor()
    imageProcessor = MarcaDagua(ProcessadorImagem)
    imageProcessor = ResizeImageProcessor(imageProcessor)
    imageProcessor.process(imagePath)

