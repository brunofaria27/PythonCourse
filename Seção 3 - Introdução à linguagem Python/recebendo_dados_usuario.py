"""
Recebendo dados do usuário

[1] - Todo dado recebido via input é do tipo String, para trabalhar com int por exemplo, você pode realizar um cast 
        Exemplo de cast Python:
        int(idade)
"""
# Entrada de dados 
print("Qual seu nome? ")
nome = input()
# nome = input("Qual seu nome? ")

print("Qual sua idade? ")
idade = input()
# idade = int(input("Qual sua idade? "))

# Processamento
nome = nome.title()

# Saída de dados 
print('Seja bem-vindo(a) %s, você tem %s anos' % (nome, idade)) 
print('Seja bem-vindo(a) {0}, você tem {1} anos'.format(nome, idade))
print(f'Seja bem-vindo(a) {nome}, você tem {idade} anos')

# Exemplo de processamento na saída dos dados
print(f'Você nasceu em {2022 - int(idade)}')