"""
Filter - Serve para filtrar os dados de uma determinada coleção
"""
import statistics # biblioteca para trabalhar com dados estatisticos

# Dados coletados de algum sensor
dados = [1.3, 2.7, 3.4, 2, 8.9, 12.9]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iteravel
res = filter(lambda x: x > media, dados)
print(list(res))
