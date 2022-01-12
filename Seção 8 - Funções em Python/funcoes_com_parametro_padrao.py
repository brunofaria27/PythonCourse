"""
Funções com parâmetro padrão

- Função onde a passagem de parametro é opcional
"""
# Função com um parametro opcional, no caso o potencia recebe um numero, caso o usuario nao passe o valor do mesmo
"""
OBS: O parametros default, devem sempre estar no final da declaração
"""
def exponencial(numero, potencia = 2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(5)) # Queremos que por padrão eleve ao quadrado
print(exponencial(5, 3)) # Senão, eleva a potencia informada pelo usuario

# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era um instrutor!'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Bruno', instrutor=False))

# Exemplos - Passando uma função por parametro
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 3, subtracao))

# ATENÇÃO COM VARIAVEIS GLOBAIS, se puder evitar, evite!
total = 0
def incrementa():
    global total # temos que inicializar a variavel no local -> global: informa que queremos utilizar a variavel global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções declaradas dentro de funções
def fora():
    contador = 0

    def dentro():
        nonlocal contador # Utilizando a variavel local contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
