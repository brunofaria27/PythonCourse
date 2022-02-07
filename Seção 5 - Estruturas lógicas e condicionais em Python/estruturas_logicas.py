"""
Estruturas Lógicas

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para 'and' ambos os valores precisam ser verdadeiros
Para 'or' ou um ou outro precisa ser verdadeiro
Para 'is' é usado para comparação de objetos (ativo is True)
"""
ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário ")
else:
    print("Você precisa ativar sua conta, cheque seu e-mail antes.")


"""
is verifica se a posição na memória é a mesma, ou seja, se é o mesmo objeto.
 - Objetos mutáveis ocupam posições diferentes na memória, mesmo que sejam semelhantes. Um exemplo disso são as listas
"""
list1 = []
list2 = []

print(f'{list1=}, {list2=}')
print(list1 == list2) # True
print(list1 is list2) # False

# Com strings (objetos imutáveis):
str1 = 'a'
str2 = 'a'

print(f'{str1=}, {str2=}')
print(str1 == str2) # True
print(str1 is str2) # True