from abc import abstractmethod
from image_processor_interface import ImageProcessorInterface

class ImageProcessorDecorator(ImageProcessorInterface):
    def __init__(self, imageProcessor: ImageProcessorInterface) -> None:
        self._imageProcessor = imageProcessor

    @abstractmethod
    def process(self, imagePath: str) -> str:
        pass