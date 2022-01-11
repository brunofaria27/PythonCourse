"""
Listas

- Listas em Python, funciona como vetores. Com a diferença de serem DINÂMICOS e podermos colocar QUALQUER tipo de dado.

Dinâmico: Não possue tamanho fixo. Ou seja, podemos criar a lista e ir adicionando elementos, podemos ir adicionando elementos enquanto o 
sistema tem memória disponível.
Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado dentro da lista.

* AS LISTAS SÃO REPRESENTADAS POR []
"""
lista1 = [1, 101, 4, 8, 19, 21, 99, 5]
lista2 = ['G', 'e', 'e', 'k', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'i', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4: 
    print(f'Encontrei o número {num}.')
else:
    print(f'Não encontrei o número {num}.')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrencias em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas
"""
OBS: Para adicionar elementos em listas usamos a função append. Com append só podemos adicionar um elemento por vez.
"""
print("Lista 1 antes de adicionar: ")
print(lista1)
lista1.append(42)
print("Lista 1 após adicionar: ")
print(lista1)

# Porém podemos colocar um elemento lista dentro de uma lista
lista1.append([12, 15, 19, 20])
print(lista1)

if [12, 15, 19, 20] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")

# Coloca cada elemento na lista como valor adicional a lista, o metódo extend só aceita iteraveis. Não aceita apenas 1 dado, como o append
lista1.extend([123, 44, 67])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
"""
Isso não substitui o valor inicial, o mesmo irá ser deslocado para a direita
"""
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista4
print("LISTA 6: ")
print(lista6)

# Podemos facilmente inverter uma lista
# Forma 1:
lista4.reverse()
print(lista4)
# Forma 2:
print(lista4[::-1])

# Podemos facilmente copiar uma lista
lista7 = lista1.copy()
print(lista7)

# Pegar o tamanho da lista
print(len(lista1))

# Remover facilmente o último elemento de uma lista
# O pop() não somente remove o último elemento, mas também o retorna
print("Antes de remover: ")
print(lista1)
lista1.pop()
print("Depois de remover: ")
print(lista1)
# Pode-se remover pelo indice, os elementos removidos são deslocados para a esquerda
"""
OBS: Se não houver elemento no indice informado, terá um erro (IndexError)
"""
lista1.pop(2)
print("Após remover indice 2: ")
print(lista1)

# Remover todos elementos da lista
lista7.clear()
print(lista7)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente converter uma String para uma Lista
"""
OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas.
"""
# Exemplo 1
curso = 'Programação Python essencial.'
print(curso)
curso = curso.split()
print(curso)
# Exemplo 2
curso2 = 'Programação,em,Python,essencial'
print(curso2)
curso2.split(',')
print(curso2)

# Convertendo uma lista em uma String
"""
OBS: Pegue a lista 8, coloque espaço (' ') entre cada elemento e crie uma String apartir disto.
"""
lista8 = ['Programação', 'em', 'Python', 'essencial']
print(lista8)
curso3 = ' '.join(lista8)
print(curso3)

# Iterando sobre listas
# Exemplo 1 (Utilizando for):
soma = 0
for elemento in lista4:
    soma = soma + elemento
print(soma)
# Exemplo 2 (Utilizando While):
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair.")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = list(range(5))
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1         2         3          4
cores = ['verde', 'amarelo', 'azul', 'vermelho', 'preto']
print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # vermelho
print(cores[4]) # preto
# Fazer o acesso de forma indexada inversa
print(cores[-1]) # preto
print(cores[-2]) # vermelho
print(cores[-3]) # azul
print(cores[-4]) # amarelo
print(cores[-5]) # verde

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# ------------------------------------
# UTEIS MAS NÃO TÃO IMPORTANTES
# Encontrar o indice de um elemento na lista
"""
OBS: Caso o item não esteja na lista irá ocorrer um erro (ValueError)
"""
numeros1 = [5, 6, 7, 8, 9, 10]
# Em qual indice da lista esta o valor 6?
print(numeros1.index(6))
# Em qual indice da lista esta o valor 9?
print(numeros1.index(9))
# Caso tenha numeros repetidos ele retorna o elemento do primeiro item encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
"""
OBS: Caso o item não esteja na lista irá ocorrer um erro (ValueError)
"""
# print(numeros1.index(6, 1)) # buscando o indice do num 5 a partir do indice 1
# print(numeros1.index(6, 2)) # buscando o indice do num 5 a partir do indice 2
# print(numeros1.index(6, 3)) # buscando o indice do num 5 a partir do indice 3
# print(numeros1.index(5, 4)) # buscando o indice do num 5 a partir do indice 4

# Podemos fazer busca a partir de um range inicio/fim
print(numeros1.index(8, 3, 6)) # buscando o indice do numero 8 entre os indices 3 a 6

# Revisão de Slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]
# Trabalhando com Slicing de lista com parametro 'inicio'
lista_slicing = [1, 2, 3, 4]
print(lista_slicing[1:]) # iniciando no indice 1 e pegando todos os elementos restantes
# Trabalhando com Slicing de lista com parametro 'fim'
print(lista_slicing[:2]) # começa em 0 e pega até o indice 2 - 1, pois o 2 não é incluso
print(lista_slicing[:4]) # começa em 0 e pega até o indice 4 - 1, pois o 4 não é incluso
print(lista_slicing[1:3]) # começa em 1 e pega até o indice 3 - 1, pois o 3 não é incluso
# Trabalhando com Slicing de lista com parametro 'passo'
print(lista_slicing[1::2]) # comeca em 1, vai até o final de 2 em 2
print(lista_slicing[0::2]) # comeca em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista
nomes = ['Bruno', 'Faria']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)

# Soma*, procurar valor max* e min*, tamanho
# *Se os valores forem todos inteiros ou reais
listar = [1, 2, 3, 4, 5, 6]
print(sum(listar)) # soma
print(max(listar)) # máximo valor
print(min(listar)) # minimo valor
print(len(listar)) # tamanho lista

# Transformar uma lista em Tupla
print(listar)
print(type(listar))
tupla = tuple(listar)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
"""
OBS: Se tivermos um número diferente de elementos na lista e de variáveis para receber os dados conseguimos um erro (ValueError)
"""
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para a outra (Shallow Copy e Deep Copy)
# Forma 1 (Deep Copy):
"""
Veja que ao utilizarmos lista.copy() copiamos os dados da lista para um nova lista, mas elas ficaram totalmente idependentes, ou seja,
modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy (Cópia profunda)
"""
lista9 = [1, 2, 3]
print(lista9)
nova1 = lista9.copy()
print(nova1)
nova1.append(4)
print(lista9)
print(nova1)
# Forma 2 (Shallow Copy):
"""
Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para uma nova lista, mas após realizar modificações em uma das listas
essa modificação se refletiu em ambas as listas. Isso em Python é chamado de Shallow Copy.
"""
lista10 = [1, 2, 3]
print(lista10)
nova2 = lista10
print(nova2)
nova2.append(4)
print(lista10)
print(nova2)