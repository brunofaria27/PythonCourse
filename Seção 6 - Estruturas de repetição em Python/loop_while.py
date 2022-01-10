"""
Loop While

Forma geral:
while expressão_booleana:
    - Execução do loop

O loop while será executado enquanto a expressão_booleana for verdadeira
Exemplo: 
num = 5

while num < 10:
    num += 1
"""
# Exemplo 1:
# Em um loop while é importante que cuidemos do critério de parada
numero = 0

while numero < 10:
    print(numero)
    numero += 1

# Exemplo 2:
resposta = ''

while resposta != 'sim':
    resposta = input("Já acabou Jessica? ")
