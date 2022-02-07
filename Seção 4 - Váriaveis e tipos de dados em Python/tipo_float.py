"""
Tipo Float
- Tipo real, decimal

Casas decimais:
OBS - O separador das casas decimais em programação é o ponto, não a vírgula
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

# Transformação de float para inteiro
"""
Ao fazer o cast de float para inteiro perdemos precisão:
- Um número 1.25 ao fazer int(1.25), perdemos as casas decimais, por exemplo.
"""
res = int(valor)
print(res)
print(type(res))

"""
Existe uma função built-in que nos permite arredondar com relativa precisão: round()
- a função funciona da seguinte forma: round(number, ndigits), tal que number é o número que queremos arredondar, e ndigits a quantidade de casas para arredondar (se for omitido, cortará todas as casas decimais).

- retorno: o valor de retorno é um inteiro se ndigits for omitido ou None. De outra forma, o valor de retorno terá o mesmo tipo de number. ndgits pode ser negativo.
"""
# Utilização padrão
valor1 = 10.39
res = round(valor1, 1)
print(res)

# Convertendo para int (mesmo que int(valor1))
res1 = round(valor1)
res2 = int(valor1)
print(f'{res1=}, {res2=}') # Funcionalidade vinda no python 3.8¹
print(res1 == res2)

# Usando ndigits negativo:
res1 = round(valor1, -1)
print(res1)

# ¹: https://docs.python.org/pt-br/3.9/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging