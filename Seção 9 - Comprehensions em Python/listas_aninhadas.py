"""
Listas Aninhadas

- Algumas linguagens de programação, possuem uma estrutura de dados chamadas de arrays:
    Unidimensionais - Arrays propriamente ditos ou vetores
    Multidimensionais - Matrizes

Em Python nós temos as listas.
"""
# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # MATRIZ 3X3
print(listas)

# Como fazemos para acessar os dados?
print(listas[0][1])
print(listas[1][2])

# Iterando Loops em listas aninhadas
for lista in listas:
    for num in lista:
        print(num)
