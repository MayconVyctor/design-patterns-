'''
03 - PADRÃO OBSERVER
====================

Conceito do Observer
--------------------
O Observer é um padrão comportamental que permite definir um mecanismo de
assinatura para notificar múltiplos objetos sobre eventos que acontecem
no objeto que estão observando.

Também conhecido como:
- Publisher-Subscriber (Pub-Sub)
- Model-View Pattern
- Dependents Pattern

Componentes:
- Subject (Sujeito): objeto que mantém lista de observers
- Observer (Observador): interface para objetos que devem ser notificados
- ConcreteObserver: implementação concreta do observer

Quando Utilizar Observer
-------------------------
✓ Quando mudanças em um objeto precisam notificar outros objetos
✓ Quando o número de objetos a notificar é desconhecido ou dinâmico
✓ Quando objetos precisam ser desacoplados
✓ Em sistemas de eventos e notificações
✓ Em arquitetura MVC (Model notifica View)

Uso em Eventos e Notificações
------------------------------
- Sistemas de notificação em tempo real
- Atualização de interfaces quando dados mudam
- Logging e auditoria
- Cache invalidation
- Implementação de callbacks

Vantagens

---------
✓ Acoplamento fraco entre Subject e Observers
✓ Princípio aberto/fechado: fácil adicionar novos observers
✓ Comunicação dinâmica: observers podem ser adicionados/removidos
✓ Suporta broadcasting (um evento para muitos listeners)

Desvantagens
------------
✗ Pode causar updates desnecessários
✗ Ordem de notificação pode ser importante e difícil de controlar
✗ Pode gerar cadeias de notificações não intencionais
'''

