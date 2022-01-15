"""
Modos de abertura de arquivo:

'r' -> abre para leitura
'w' -> abre para escrita - sobrescreve, caso o arquivo já exista
'x' -> abre para escrita, somente se o arquivo não existir. Caso exista, gera FileExistsError
'a' -> abre para escrita, adicionando o conteúdo no final do arquivo
'+' -> abre para o modo de atualização: Leitura e escrita (temos controle do cursor)
"""