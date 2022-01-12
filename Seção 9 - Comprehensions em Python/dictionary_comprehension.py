"""
Dictionary Comprehension

# Sintaxe:
{chave:valor for valor in iteravel}
"""
# Exemplo
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Exemplo 2
numbers = [1, 2, 3, 4, 5, 6]
quadrados = {valor: valor ** 2 for valor in numbers}
print(quadrados)

# Exemplo 3:
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional
number = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in number}
print(res)