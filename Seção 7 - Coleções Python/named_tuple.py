"""
Módulos Collections - Named Tuple

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e tambem os parametros 
"""
from collections import namedtuple

# Definindo nome e parametros
# Forma 1:
cachorro = namedtuple('cachorro', 'idade raca nome')
# Forma 2:
cachorro = namedtuple('cachorro', 'idade, raca, nome')
# Forma 3:
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow Chow', nome='ray')
print(ray)

# Acessando os dados
# Forma 1:
print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome
# Forma 2:
print(ray.idade)
print(ray.nome)
print(ray.raca)