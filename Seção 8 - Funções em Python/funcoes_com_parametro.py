"""
Funções com parâmetro
"""
# Função com parametro
def quadrado(numero):
    return numero ** 2

print(quadrado(5), quadrado(2))

# Função parabéns refatorada
def cantar_parabens(aniversariante):
    print("Parabéns para você.")
    print("Nesta data querida,")
    print("Muitas felicidades")
    print("Muitos anos de vida!")
    print(f'AEEEEE !!!! Viva o {aniversariante}')

print(cantar_parabens('Bruno'))

# Mais exemplos
def soma(a, b):
    return a + b

print(soma(2, 5))


def multiplicacao(num1, num2):
    return num1 * num2

print(multiplicacao(2, 2))


def outra(num1, b, msg):
    return (num1 + b) * msg
    
print(outra(2, 3, 'Amando a linguagem Python '))
print(outra(msg='Testando! ', b=1, num1=2)) # Neste caso não precisa estar na ordem correta pois estamos passando o valor para cada variavel da funcao msg='recebe', "ARGUMENTOS NOMEADOS"