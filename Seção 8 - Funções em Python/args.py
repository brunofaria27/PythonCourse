"""
Entendendo o *args

- O parametro *args é um parametro qualquer. Isso significa que voce poderá chamar de qualquer coisa, desde que comece com *
Exemplo: 
Podemos colocar *xis, mas a comunidade decidiu utilizar *args

Mas o que é o *args?
- O parâmetro *args é utilizado em um função, coloca os valores extras informados como entrada em uma tupla. Então, lembre-se desde já que tuplas são imutáveis.
- O asterisco serve para informar ao Python que estamos passando uma coleção de dados, por isso ele sabe que precisa desempacotar estes antes.
"""
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(1, 2, 3))
# print(soma_todos_numeros(1, 2, 3, 4)) -> TypeError
# print(soma_todos_numeros(1, 2)) -> TypeError

# Entendendo o args
def soma_todos_os_numeros(*args):
    # sum(args)
    total = 0
    for numeros in args:
        total = total + numeros
    return total

print(soma_todos_os_numeros(1, 1, 2, 3, 4, 5, 1, 2))

# Exemplo
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não sei quem você é infelizmente!'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
