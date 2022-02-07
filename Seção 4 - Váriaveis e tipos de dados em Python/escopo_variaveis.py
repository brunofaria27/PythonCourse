"""
Escopo de váriaveis

Dois casos de escopo:
    [1] - Váriaveis Globais:
    - São reconhecidas por todo o programa.

    [2] - Váriaveis Locais:
    - Reconhecidas apenas no bloco onde foi declarada.

Para declarar váriavel em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao colocarmos um valor a váriavel, nós não colocamos o tipo de dado dela. Este tipo é inferido ao atribuirmos o valor a ela.
"""
# Váriavel global (numero)
numero = 2

# Variavel local (novo)
if numero > 10:
    novo = numero + 10
    print(novo)

# Erro -> a váriavel novo vai dar como não declarada
print(novo)