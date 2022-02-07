"""
Tipo Boolean:
- Álgebra Booleana -> 2 constantes (True or False)
OBS: Sempre com a primeira letra maíuscula
"""
ativo = True
print(ativo)

# Operações básicas
# Negação (not):
"""
Fazendo a negação, se o valor boolean for verdadeiro a resposta será falsa, se for falso será verdadeiro, ou seja sempre o contrário. (Equivalente a ~proposição, na matemática)
"""
print(not ativo)

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores, ou um ou outro deve ser verdadeiro.

True  or True  -> True
True  or False -> True
False or True  -> True
False or False -> False
"""
logado = False
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores, ambos devem ser True.

True  and True  -> True
True  and False -> False
False and True  -> False
False and False -> False
"""
print(ativo and logado)
print(ativo and not logado)