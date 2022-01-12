"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iteravel.
# Sintaxe:
[dado for dado in iteravel]
"""
# Exemplos
"""
Para cada numero na lista de numeros ele esta multiplicando por 10 e guardando na lista res
"""
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
res = [numero / 2 for numero in numeros]
print(res)

# List Comprehension VS Loop
# Loop
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)
# List Comprehension
print([numero * 2 for numero in numeros])

# Exemplo:
nome = 'Geek University'
print([letra.upper() for letra in nome])
# Exemplo 2:
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['gabriel', 'tadeu', 'pedro', 'demetrio']
print([caixa_alta(amigo) for amigo in amigos])

"""
List Comprehension - Parte II

- Podemos adicionar estruturas condicionais lógicas a nossa List Comprehension
"""
# Exemplos
numbers = [1, 2, 3, 4, 5, 6]
pares = [number for number in numbers if number % 2 == 0]
impares = [number for number in numbers if number % 2 != 0]
print(pares)
print(impares)
# Refatorar
# Qualquer número par modulo de 2 é 0 e 0 em python e False. not False = True
pares = [number for number in numbers if not number % 2]
# Qualquer número ímpar módulo de 2 é 1 e 1 em python e True 
impares = [number for number in numbers if number % 2]
print(pares)
print(impares)

# Exemplo 2:
res = [number * 2 if number % 2 == 0 else number / 2 for number in numbers]
print(res)