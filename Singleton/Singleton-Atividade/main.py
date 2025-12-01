from authManager import AuthManager

if __name__ == '__main__':
    print("TESTE DO PADRÃO SINGLETON: AuthManager")
    print("=" * 50)

    auth1 = AuthManager().getInstance()
    auth2 = AuthManager().getInstance()
    print(f" auth1 é a mesma instância que auth2? → {auth1 is auth2}")
    print("-" * 40)

    print("Registro de usuários")
    print("-" * 40)
    auth1.registrar("mike", "mike123", "comum")
    auth2.registrar("livia", "livia123", "comum")
    auth1.registrar("Maycon", "mayconpassword", "admin")

    print("Usuários registrados com sucesso:")
    for login, dados in auth1.todosUsuariosRegistrados().items():
        print(f"  {login} → tipo: {dados['tipo']}")
    print("-" * 40)

    print("Tentativas de login")
    print("-" * 40)
    print(f" mike tenta logar com senha correta: {auth1.login('mike', 'mike123')}")
    print(f" livia tenta logar com senha errada: {auth2.login('livia', '123LIVIA')}")
    print(f" Maycon tenta logar com senha correta: {auth1.login('Maycon', 'mayconpassword')}")

    print("-" * 40)
    print("Usuarios autenticados apos logins:")
    logados = auth1.usuariosAutenticados()
    if logados:
        for user in logados:
            print(f"{user}")
    else:
        print("   (nenhum usuário autenticado)")

    print("-" * 40)
    print(" Verificação de status individual")
    print("-" * 40)
    print(f"→ mike está logado? {auth1.estaLogado('mike')}")
    print(f"→ livia está logada? {auth2.estaLogado('livia')}")
    print(f"→ Maycon está logado? {auth1.estaLogado('Maycon')}")

    print("-" * 40)
    print("Logout de um usuario")
    print(f"→ mike faz logout...")
    auth1.logout("mike")
    print(f"✔ mike está logado após logout? {auth2.estaLogado('mike')}")

    print("-" * 40)
    print(" Usuários autenticados agora:")
    for user in auth2.usuariosAutenticados():
        print(f"   • {user}")

