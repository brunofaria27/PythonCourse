"""
Criando sua própria versão de Loops
"""
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Bruno Faria':
    print(letra)

# Criando nosso Loop
def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek University')

numeros = [12, 14, 1, 21]
meu_for(numeros)