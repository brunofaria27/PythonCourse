"""
Saindo de loops com breaks
- Funciona da mesma forma que a linguagem C ou Java.
- Usamos o break para sair de um loop de maneira projetada.
"""
# Exemplo 1
for num in range(1, 11):
    if num == 6:
        print("Achei num 6.")
        break   # Saia do loop
    else:
        print(num)

# Exemplo 2
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break   # Se comando for igual a sair, sai do loop

"""
Continue -> instrução que interrompe a iteração atual do loop e faz o programa retornar ao topo do loop.
"""
# Exemplo:
for n in range(5):
    if n == 3:
        continue

    print(f'Executando em... {n}')


# Exemplo de continue e break no mesmo laço: 
while True:
    nome = input("Digite seu nome: ")
    comando = input("Digite 'voltar' para mudar de nome e 'sair' para parar. Senão, dê enter: ")
    if comando == 'voltar':
        continue
    elif comando == 'sair':
        break

    print(f'Seu nome é {nome}!')