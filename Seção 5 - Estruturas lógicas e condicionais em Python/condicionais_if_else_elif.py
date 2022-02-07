"""
Estruturas condicionais
if, else, elif
"""
idade = 17

# if-elif-else
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos de idade")
else:
    print("Maior de idade")

#if-if-else
if idade < 18:
    print("Menor de idade")
if idade != 18:
    print("Tem idade diferente de 18")
else:
    print("Maior de idade")