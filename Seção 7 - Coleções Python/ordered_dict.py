"""
Módulos Collections - Ordered Dict

Ordered Dict -> Dicionario que nos garante a ordem de insercao dos elementos, ou seja, a ordem importa
"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items(): 
    print(f'chave={chave} e valor={valor}')