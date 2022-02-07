"""
Dunder -> double underscore

Exemplo: 

Dunder Name e Dunder Main
Dunder Name -> __name__
Dunder Main -> __main__

Em Python, são utilizados double underscore para criar funções, atributos, propriedades e etc para não gerar conflito com os nomes desses elementos na programação.

São conhecidos também por métodos especiais e métodos mágicos.

Se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.
É por isso que costumamos ver: 

if __name__ == '__main__':
    código (geralmente de teste)
"""