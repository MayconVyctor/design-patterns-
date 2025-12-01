class AuthManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance._usuariosRegistrados = {}
            cls._instance._loginsUsuariosAutenticados = []

        return cls._instance

    def getInstance(self):
        return self._instance

    def registrar(self, login: str, senha: str, tipo: str):
        self._usuariosRegistrados[login] = {
            "senha": senha,
            "tipo": tipo
        }

    def login(self, login: str, senha: str):
        usuarioAux = self._usuariosRegistrados.get(login)
        logado = False
        if usuarioAux is not None:
            if usuarioAux["senha"] == senha:
                logado = True
                # Adiciona o login do usuário à lista de autenticados
                if login not in self._loginsUsuariosAutenticados:
                    self._loginsUsuariosAutenticados.append(login)
        return logado

    def usuariosAutenticados(self):
        return list(self._loginsUsuariosAutenticados)

    def estaLogado(self, login: str):
        return login in self._loginsUsuariosAutenticados

    def logout(self, login: str):
        if login in self._loginsUsuariosAutenticados:
            self._loginsUsuariosAutenticados.remove(login)

    def todosUsuariosRegistrados(self):
        return self._usuariosRegistrados