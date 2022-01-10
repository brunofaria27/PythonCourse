"""
Tipo String

Um dado é considerado tipo String quando:
- Estiver entre Aspas simples -> 'Bruno Faria'
- Estiver entre Aspas duplas -> "Bruno Faria"
- Estiver entre Aspas simples triplas -> '''Bruno Faria'''
- Estiver entre Aspas duplas triplas
"""
# Acrescentar em uma lista de Strings cada parte separada por espaço
nome = "Bruno Rodrigues Faria"
print(nome.split())

print(nome[0:5])    # Slice de String
print(nome[6:15])   # Slice de String
print(nome[16:21])  # Slice de String

# [0,         1,           2]
#  ['Bruno', 'Rodrigues', 'Faria']
print(nome.split()[2])

"""
[::-1] -> Começe do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])

# Inverter o último nome
ultimo_nome = nome.split()[2]
print(ultimo_nome[::-1])
print(nome.split()[2][::-1])

# Substituir a letra R pela letra W
nome = nome.lower().replace('r', 'w')
print(nome.title())