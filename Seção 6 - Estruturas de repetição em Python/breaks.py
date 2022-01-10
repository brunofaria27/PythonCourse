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
