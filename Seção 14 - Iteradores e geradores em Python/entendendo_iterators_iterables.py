"""
Etendendo Iterators e Iterables

Iterators ->
    Formalmente:
        - é um objeto com o método next (python 2) ou __next__ (python 3)
    
    informalmente:
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterables ->
    Formalmente:
        - É um objeto com o método __iter__, que retorna um iterator, ou que defina o método __getitem__, que pode pegar índices sequenciais começando de zero (e ascende (raise) IndexError quando os índices não são mais válidos).
    Informalmente:
    - Um objeto que pode retornar um iterator quando a função iter() for chamada.
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
