"""
Set Comprehension
"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 2:
numeros = {num ** 2 for num in range(10)}
print(numeros)

# DESAFIO! Faça uma mudança na estrutura acima para gerar um dicionario ao inves de um set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Último exemplo
letras = {letra for letra in 'Bruno Faria'}
print(letras)