from .constructor.introductionProcess import introductionProcess

def start():
  #  while True:
        comand = introductionProcess()

        match comand:
            case 1:
                "chamar uma operacao que registra"
                peopleRegisterConstructor()
                pass
            case 2:
                "chamar uma operacao que buscar"
                peopleFinderConstructor()
                pass
            case 5:
                exit()

            case _ :
                pass


