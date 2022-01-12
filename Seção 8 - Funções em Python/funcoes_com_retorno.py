"""
Funções com retorno
"""
# Função retornando valor
# Exemplo 1:
def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())
# Exemplo 2: Diferentes returns
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())
# Exemplo 3: Retornando multiplos valores
def outra_funcao():
    return 1, 2, 3, 4

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# Criar uma função para jogar uma moeda
from random import random

def joga_moeda():
    valor = random() # Gera um número random entre 0 e 1
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Codificação desnecessária - colocar um else no caso de baixo
def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())