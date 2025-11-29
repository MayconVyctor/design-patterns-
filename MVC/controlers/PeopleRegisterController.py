from typing import Dict
class PeopleRegisterController:
    def register(self, newPersonInformatio: Dict):
        self.validateFields(newPersonInformatio)
        self.createPersonAndStore(newPersonInformatio)

    def validateFields(newPersonInformatio):
        if not isinstance(newPersonInformatio["name"], str):
            raise Exception('Campo Nome Incorreto!')

        try:
            int(newPersonInformatio["age"])
        except:
            raise Exception('Campo Idade Incorreto!')

        try:
            float(newPersonInformatio["height"])
        except:
            raise Exception('Campo Altura Incorreto!')
    def createPersonAndStore(self, newPersonInformatio: Dict):
        name = newPersonInformatio["name"]
        # Garante que os tipos estejam corretos conforme a entidade Person
        age = int(newPersonInformatio["age"])
        height = float(newPersonInformatio["height"])

        new_person = Person(name, age, height)
        person_repository.registry_person(new_person)
