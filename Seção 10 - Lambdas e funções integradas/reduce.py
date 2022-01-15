"""
Reduce - 'functools'
- Como se fosse uma função 'recursiva'
"""
from functools import reduce

dados = [2, 3, 4, 5, 7, 10, 23, 45, 65, 75, 98, 120]

# Para utilizar o reduce temos que ter uma função que receba dois parametros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

