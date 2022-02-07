"""
Else / Finally / Try / Except
"""
# else: executado sempre que não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')

# Finally: sempre executado. Independente se houver ou não a exception
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto.')
else:
    print(f'Você digitou {num}')
finally:
    print("Sempre sou executado.")


#OBS: O finally é geralmente utilizado para fechar ou desalocar recursos, banco de dados, por exemplo. 