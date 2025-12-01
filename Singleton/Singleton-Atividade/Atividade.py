'''''
Objetivo:
Implementar o padrão de projeto Singleton em Python para gerenciar um recurso
compartilhado na aplicação.
Descrição da Tarefa:
Desenvolva uma classe Singleton conforme um dos dois cenários abaixo:
1. Gerenciamento de Autenticação
○ Crie uma classe AuthManager Singleton que mantenha um dicionário em
memória com os dados de login de usuários.
○ A classe deve permitir:
■ Registrar (login) um usuário com nome de usuário e senha (ou token).
■ Verificar se já existe um usuário logado ou obter o usuário atual.
■ Efetuar logout.
○ Todos os módulos da aplicação que acessarem a instância do AuthManager
devem ver o mesmo estado (ou seja, a mesma instância).
2. Logger Global para Arquivo
○ Crie uma classe FileLogger Singleton que grava mensagens de log em um
arquivo.
○ A classe deve permitir:
■ Registrar mensagens de diferentes níveis (por exemplo: info,
warning, error).
■ Abrir (ou manter aberto) um arquivo de log único onde todas as
mensagens são gravadas.
■ Garantir que múltiplas partes da aplicação (módulos) usem
exatamente a mesma instância do logger e, consequentemente,
gravem no mesmo arquivo.
Requisitos Técnicos:
● Use o método mágico __new__ para garantir que apenas uma instância da classe
Singleton seja criada.
● Não use bibliotecas externas para implementar o Singleton: a lógica de instância
única deve estar no seu código.
● Escreva um pequeno script de exemplo (main) que demonstre:
○ No caso da AuthManager: login, obtenção do usuário atual e logout.
○ No caso do FileLogger: escrever algumas mensagens de log e mostrar
que todas vão para o mesmo arquivo.
'''