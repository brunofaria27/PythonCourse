"""
Leitura de arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open('caminho_a_ser_lido') -> O arqiovo a ser lido deve existir
"""
# Exemplo utilização
arquivo = open('arquivo_para_testes.txt')

# Para ler o conteúdo de um arquivo, apos a abertura, devemos utilizar a função read()
# A função read ler todo o conteúdo do arquivo, se for executado novamente não irá retornar nada, pois todo o conteúdo do arquivo já foi lido.
# print(arquivo.read())
# Para arrumar isso podemos armazenar em uma String
ret = arquivo.read().split('\n') # Lê e coloca cada uma das linhas em uma String
print(ret)

# Fechando o arquivo - ESSENCIAL
arquivo.close()
