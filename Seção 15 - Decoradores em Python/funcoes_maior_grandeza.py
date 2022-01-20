"""
Funções de maior grandeza (Higher Order Functions - HOF)

O que isso significa? 
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como resultado ou mesmo que podemos passar
outras funções como argumentos para outras funções, e até mesmo criar variaveis do tipo funções no nossos programas.

OBS: Na seção de funções, nós utilizamos isso.
"""
# Definindo funções
def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funcoes
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nasted Functions - Funções Aninhadas
# Em Python podemos ter funções dentro de funções.
# Exemplo;
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Bruno'))
print(cumprimento('Gustavo'))
