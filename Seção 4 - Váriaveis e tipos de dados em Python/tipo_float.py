"""
Tipo Float
- Tipo real, decimal

Casas decimais:
OBS - O separador das casas decimais em programação e ponto e não é uma vírgula
"""
# Não é reconhecido como float 
valor = 1, 44
print(valor)
print(type(valor))

# É reconhecido como float 
valor = 1.44
print(valor)
print(type(valor))

# Dupla atribuição
valor1, valor2 = 1, 44
print(valor)
print(type(valor2))
print(valor1)
print(type(valor1))

# Podemos converter float para inteiro
"""
Ao fazer o cast de float para inteiro perdemos precisão:
- Um número 1.25 ao fazer int(1.25), perdemos as casas decimais, por exemplo.
"""
res = int(valor)
print(res)
print(type(res))