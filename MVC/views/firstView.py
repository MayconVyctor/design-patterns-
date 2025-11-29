
def introductionPage():
    message = '''
            Sistema Cadastral

            * 1 - Cadastrar Pessoa
            * 2 - Buscar Pessoa Por Nome
            * 5 - Sair
        '''
    print(message)
    comand = input("Comando")
    return comand