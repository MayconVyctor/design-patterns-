
from imageProcesorDecorator import ImageProcessorDecorator

class WatermarkImageProcessor(ImageProcessorDecorator):
    """Processador de imagem com marca d'água"""

    #def __init__(self, imageProcessor: ImageProcessorInterface):   - ja foi criando na classe pai
     #   self._imageProcessor = imageProcessor

    def process(self, imagePath: str) -> str:
        ImageProcessedPath = self._imageProcessor.process(imagePath)
        
        #TODO: Implementa a lógica da marca d'água
        newImagePath = "/uploads/watermark_file.jpg"
         
        print(f"Processa a imagem de {ImageProcessedPath} para {newImagePath}")
        
        return newImagePath