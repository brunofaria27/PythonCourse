"""
Conjuntos

- Conjuntos em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos em matemática
- Os conjuntos no Python, são chamados de Sets.

Da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indices, ou seja, conjuntos não são indexados;

Conjuntos são bons para utilizar quando precisamos armazenar elementos mas não nós importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos (Sets) em Python são referênciados por {}

Diferença entre conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um dicinario tem chave e valor
    - Um conjunto tem apenas valor
"""
# Definindo conjuntos em Python:
# Forma 1:
s = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 7}) # Repare que temos valores repetidos
print(s)
# Forma 2 (Mais comum):
s = {1, 2, 3, 4, 4, 5, 2}
print(s)

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar que além de não termos valores duplicados não temos ordem
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2 ,34] # Aceita valor duplicado
print(f'Lista: {lista} com {len(lista)} elementos.')
tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34) # Aceita valor duplicado
print(f'Tupla: {tupla} com {len(tupla)} elementos.')
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2 ,34], 'dict') # Não aceita chaves duplicadas
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos.')
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34} # Não aceita valor duplicado
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos.')

# Assim como outro conjunto Python podemos misturar vários tipos de dados misturados em Sets

# Usos interessantes com Sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museum e os visitantes informam manualmente as cidades de onde vieram
# Nós adicionamos cada cidade em um lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.
cidades = ['Belo Horizonte', 'Cuiabá', 'São Paulo', 'São Paulo', 'São Paulo', 'Belo Horizonte']
print(cidades)
# Agora precisamos saber quantas cidades únicas tem-se na lista.
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s1 = {1, 2, 4}
s1.add(3)
s1.add(3) # Duplicidade não gera erro, apenas é ignorado
print(s1)

# Remover elementos de um conjunto
# Forma 1:
s1.remove(3) # Informamos o valor a ser removido -> Não encontrado = KeyError
print(s1)
# Forma 2:
s1.discard(2) # Se o valor não for encontrado, nenhum erro é gerado
print(s1)

# Copiando um conjunto para outro
# Forma 1 (Deep Copy):
novo = s1.copy()
print(novo)
novo.add(4)
print(novo)
print(s1)
# Forma 2 (Shallow Copy):
novo1 = s1
novo1.add(5)
print(novo1)
print(s1)

# Removendo todos os itens de um conjunto
s1.clear()
print(s1)

# Metódos matemáticos de conjuntos
# Temos dois conjuntos: Estudantes Python, Estudantes Java
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Veja que alguns alunos estudam Java e Python
# Precisamos criar um conjunto com nomes de estudantes unicos
# Forma 1 - Usando UNION
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_java | estudantes_python
print(unicos2)
# Gerar um conjunto de estudantes que estão em ambos os cursos 
# Forma 1 - Utilizando Intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)
# Gerar um conjunto de estudantes que não estão em 2 cursos ao mesmo tempo
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, procurar valor max* e min*, tamanho
# *Se os valores forem todos inteiros ou reais
s2 = {1, 2, 3, 4, 5, 6}
print(sum(s2)) # soma
print(max(s2)) # máximo valor
print(min(s2)) # minimo valor
print(len(s2))          # tamanho do dicionario