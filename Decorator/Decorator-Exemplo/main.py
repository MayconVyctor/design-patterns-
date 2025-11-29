from processadorImagemEscalaCinza import EscalaCinza
from Decorator.redimencionarImagem import RedimencionarImagem

imagem = EscalaCinza("imagem.jpg")
imagem = RedimencionarImagem(imagem)
imagem.procesar()
