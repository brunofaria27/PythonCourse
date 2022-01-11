"""
Mapas - conhecidos em Python por dicionários
"""
receita = {'jan':120, 'fev':232, 'mar':92}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Ter acesso a todas as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Ter acesso a todos os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, procurar valor max* e min*, tamanho
# *Se os valores forem todos inteiros ou reais
print(sum(receita.values())) # soma
print(max(receita.values())) # máximo valor
print(min(receita.values())) # minimo valor
print(len(receita))          # tamanho do dicionario