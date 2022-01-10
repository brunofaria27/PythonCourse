"""
Loop for

EMOJI UNICODE: https://apps.timwhitlock.info/emoji/tables/unicode
"""
nome = 'Geek University'
lista = [1, 2, 4, 5, 7, 12, 20]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Primeiro exemplo de for -> para cada letra (posição) dentro de nome imprima a posição
for letra in nome:
    print(letra)

# Segundo exemplo de for (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Terceiro exemplo de for (Iterando sobre um range)
"""
Range(valor_inicial, valor_final)

OBS: O valor final não é inclusive, ou seja, não está incluso.
"""
for numero in range(1, 10):
    print(f'{numero} ', end='') # end='' -> faz com que você não pule linha no console

# Enumerate
"""
((0, 'G'), (1, 'e'), (2, 'e') ...)
Ou seja, para cada sequencia do nosso interavel ele atribui um indice
"""
for i, letra in enumerate(nome):
    print(nome[i])

for i, letra in enumerate(nome):
    print(letra)

# Exemplo usando uma condicional dentro do for
contador = 0
for i, letra in enumerate(nome):
    if nome[i] == 'e':
        contador += 1
print(f'Foi achado {contador} letras E no nome')

# Usuário definindo loop
qtd = int(input("Quantas vezes o loop deve executar: "))

for i in range(0, qtd):
    print(f'Imprimindo {i + 1} vezes.')

# Soma atráves de um for
soma = 0

for i in range(0, 3):
    num = int(input(f'Informe o valor {i + 1}: '))
    soma += num
print(f'A soma foi de {soma}.')

# Emoji no console
# Original: U+1F60D
# Modificado: U0001F60D
for i in range(0, 10):
    print('\U0001F60D ' * i)