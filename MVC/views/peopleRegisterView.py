import os
from typing import Dict
class PeopleRegisterView:
    def registryPersonView(self):

        os.system("clear")
        print(" Registry Person ")
        name = input("Please enter your name: ")
        age = input("Please enter your age: ")
        heigth = input("Please enter your heigth: ")

        newPersonInformation = {
            "name": name, "age": age, "height": height
        }

        return newPersonInformation