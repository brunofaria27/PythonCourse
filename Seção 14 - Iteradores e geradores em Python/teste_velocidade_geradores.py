"""
Teste de velocidade usando expressões geradoras
"""
def nums():
    for num in range(1, 10):
        yield num

gel = nums()
print(gel) # Generator
print(next(gel))
print(next(gel))

# Generator Expression
ge2 = (num for num in range(1, 10))
print(ge2) # Generator Expression
print(next(ge2))
print(next(ge2))

# Soma dos números de 1 a 9
print(sum(num for num in range(1, 10)))

# Testes de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1_000_000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(1_000_000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')