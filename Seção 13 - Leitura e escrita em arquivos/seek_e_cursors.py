"""
Seeks e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.
"""
arquivo = open('arquivo_para_testes.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo, recebe um parametro onde colocaremos o cursor no arquivo
arquivo.seek(0)
print(arquivo.read())

# readline() -> Lê o arquivo linha a linha
arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())

# readlines() -> le todas a linhas e armazena em uma lista
arquivo.seek(0)
lista_de_linhas = arquivo.readlines()
print(lista_de_linhas)

# Fechando o arquivo após trabalhar com o mesmo
arquivo.close()

if arquivo.closed:
    print('O arquivo está fechado')
else:
    arquivo.close()
    print(arquivo.closed) # True -> verifica se o arquivo está fechado
