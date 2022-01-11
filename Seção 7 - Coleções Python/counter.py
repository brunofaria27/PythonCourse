"""
Módulos Collections - Counter

Collections -> High-Performace Container Datetypes
Counter ->  Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada como parametro
e como valor a quantidade de ocorrencias desse elemento 
"""
# Utilizando o counter
from collections import Counter

# Podemos utilizar qualquer iteravel aqui
lista = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 1, 2, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1]

# Utilizando o counter
res = Counter(lista)
print(res)