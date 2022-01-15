"""
Else / Finally / Try / Except
"""
# Executando sempre que não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')
finally:
    print("Sempre sou executado.")

# OBS: O bloco finally é sempre executado. Independente se houver ou não a exception
# O finally e geralmente utilizado para fechar ou desalocar recursos, banco de dados, por exemplo. 