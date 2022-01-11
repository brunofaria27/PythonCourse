"""
Módulos Collections - Default Dict

Default Dict -> Ao criar um dicionario utilizando-o, nós imformamos um valor default, podendo utilizar uma lambda para isso. Esse valor será utilizado sempre que não tiver um valor 
definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido.

OBS: Lambdas são funcões sem nomes que podem ou não receber parametros de entradas e retornar valores.
"""
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario['curso'])
# print(dicionario['chave']) # Key Error

from collections import defaultdict

dicionario1 = defaultdict(lambda: 0)
print(dicionario1)
dicionario1['curso'] = 'Programa do Bruno'
print(dicionario1)
print(dicionario1['outro'])
print(dicionario1)