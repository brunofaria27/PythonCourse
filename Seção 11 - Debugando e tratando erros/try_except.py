"""
Bloco Try/Except

- Como se fosse um try/catch do Java
"""
# Exemplo 1 - Tratando erro generico:
try:
    geek()
except:
    print('Deu algum prblema.')

# Exemplo 2 - Pode-se especificar o tipo de erro:
try:
    geek()
except NameError as err:
    print(f'Utilizando uma função inexistente. Erro: {err}')

# Exemplo real:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as error:
        return None
    except:
        return None

dic = {"nome": "Bruno"}
print(pega_valor(dic, 'nome'))
