"""
Tuplas (Tuple)

- Tuplas são bastante parecidas com listas, existem basicamente duas diferenças.
[1] - As tuplas são representadas por parênteses ().
[2] - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla cria uma nova tupla.
"""
# CUIDADO 1:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
"""
CONCLUSÃO: Podemos concluir que uma tupla e definida pelo o uso da vírgula, mas não pelo uso do parênteses.
"""
tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))
tupla4 = (4, ) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# Criando tupla dinamicamente usando range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla
"""
Gera ValueError se colocar um numero diferente de elementos para desempacotar.
"""
tupla5 = ('Geek University', "Programação em Python: Essencial")
escola, curso = tupla5
print(escola)
print(curso)

"""
Metódos de adição e remoção em tuplas não existem, dado o fato de tuplas serem imutáveis.
"""
# Soma*, procurar valor max* e min*, tamanho
# *Se os valores forem todos inteiros ou reais
tupla6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(sum(tupla6)) # soma
print(max(tupla6)) # máximo valor
print(min(tupla6)) # minimo valor
print(len(tupla6)) # tamanho lista

# Concatenação de Tuplas
tupla7 = 1, 2, 3
tupla8 = 4, 5, 6
print(tupla7)
print(tupla8)
print(tupla7 + tupla8)
tupla7 = tupla7 + tupla8
print(tupla7) # Tuplas são imutaveis mas podemos sobrescrever seus valores

# Verificar se determinado elemento está contido na tupla
tupla9 = 1, 2, 3
print(3 in tupla9)

# Iterando sobre um tupla 
tupla10 = 1, 2, 3, 4, 5
for n in tupla10:
    print(n)

for indice, valor in enumerate(tupla10):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla11 = 'a', 'a', 'b', 'a', 'c', 'e', 'w'
print(tupla11.count('a'))
universidade = tuple('PUC Minas')
print(universidade)
print(universidade.count('i'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos mudar os dados contidos em uma coleção
# Exemplo: Meses do ano
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante ao da lista
print(meses[6])

# Iterar com While
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar em qual indice um elemento esta na tupla
"""
OBS: Caso o elemento não existe terá o erro (ValueError)
"""
print(meses.index('Fevereiro'))

# Podemos utiliza Slicing em Tupla como em Lista
# tupla[inicio:fim:passo]
print(meses[5:9])

"""
Por que utilizar tuplas?
- Tuplas são mais rápidas que listas.
- Tuplas deixam seu código mais seguro.
- Isso porque trabalhar com elementos imutáveis traz segurança ao código.
"""

# Copiando uma lista para a outra:
# Na tupla não temos o problema de Shallow Copy
tupla12 = 1, 2, 3
print(tupla12)
nova = tupla12
print(nova)
print(tupla12)
outra = 4, 5, 6
nova = nova + outra
print(nova)
print(tupla12)