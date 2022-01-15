"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software, precisa ter permissão:
    - Leitura
    - Escrita

StringIO -> Utilizados para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO
from tokenize import String

# Utilizando
mensagem = 'Esta é apenas uma String normal.'

# Podemos criar um arquivo em memória já com a string inserida, ou mesmo vazio para inserirmos depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora, tendo o arquivo podemos utilizar tudo que conhecemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('\nOutro texto')

# Podemos movimentar o cursor
arquivo.seek(0)

# Leitura após modificações
print(arquivo.read())

# Fechando o arquivo
arquivo.close()
