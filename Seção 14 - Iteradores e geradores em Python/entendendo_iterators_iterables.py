"""
Etendendo Iterators e Iterables

Iterators ->
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterables ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""
nome = 'Geek' # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5] # É um iterator mas não é um iterable

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for letra in nome:
    print(f'{letra}')

