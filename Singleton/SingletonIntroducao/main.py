from Singleton.SingletonIntroducao.IntroDesingPatersn import BDManager

bd1 = BDManager()
conexao1 = bd1.getInstancia("/caminho!")

bd2 = BDManager()
conexao2 = bd2.getInstancia("/caminho!")

print(f"Objetos 1: {conexao1._id}, Objeto 2: {conexao2._id}")
print(f"Objetos 1: {id(conexao2)} == Objeto 2: {id(conexao2)}")
