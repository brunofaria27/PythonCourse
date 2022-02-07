"""
Ranges

- Precisamos conhecer o loop para usar o range 
- Precisamos conhecer os ranges para trabalhar melhor com os loops

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.
Formas gerais:
[1] - range(valor_de_parada)
OBS: O valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

[2] - range(valor_de_inicio, valor_de_parada)
OBS: O valor_de_parada não inclusive

[3] - range(valor_de_inicio, valor_de_parada, passo)
OBS: O valor_de_parada não inclusive (passo é especificado pelo usuário)

[4] - range(valor_de_inicio, valor_de_parada, passo)
OBS: O valor_de_parada não inclusive (valor_de_inicio é especificado pelo usuário, passo é especificado pelo usuário)
"""
# Forma 1
for num in range(11):
    print(num)

print("----------------------")

# Forma 2
for num in range(0, 10):
    print(num)

print("----------------------")

# Forma 3
for num in range(1, 10, 2):
    print(num)

print("----------------------")

# Forma 4 - Decrementando (Inverso)
for num in range(10, -1, -2):
    print(num)

print("----------------------")

"""
Podemos inclusive construir objetos em cima de range:
"""
lista = list(range(10))
tupla = tuple(range(10))
conjunto = set(range(10)) # Será apresentado depois, mas é o conjunto matemático

print(lista)
print(tupla)
print(conjunto)