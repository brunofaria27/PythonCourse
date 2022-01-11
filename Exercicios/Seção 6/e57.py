# Entrada de dados
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

# Processamento 
contador = 0
numeros = 0

for num in range(a, b):
    if contador == 2:
        numeros += 1
    contador = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            contador += 1

# Saída de dados
print(f'Tem entre o intervalo [{a}, {b}], {numeros} primos. ')
