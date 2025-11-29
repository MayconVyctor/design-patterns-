
from imageProcesorDecorator import ImageProcessorDecorator

class ResizeImageProcessor(ImageProcessorDecorator):
    """Processador de imagem com redimensionamento"""

   # def __init__(self, imageProcessor: ImageProcessorInterface): - ja esta feito na classe pai
    #    self._imageProcessor = imageProcessor

    def process(self, imagePath: str) -> str:
        ImageProcessedPath = self._imageProcessor.process(imagePath)
        
        #TODO: Implementa a lógica do redimensionamento
        newImagePath = "/uploads/resized_file.jpg"
         
        print(f"Processa a imagem de {ImageProcessedPath} para {newImagePath}")
        
        return newImagePath