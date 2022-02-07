"""
Lambdas - Funções anônimas (sem nome)
"""
# Expressão lambda
lambda x: 3 * x + 1 # Recebe x e retorna (3 * x + 1)

# Como utilizar a expressão lambda
calc = lambda x: 3 * 3 * x
print(calc(10))
print(calc(2))

# Múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().tilte() + ' ' + sobrenome.strip().title()
print(nome_completo('Bruno', 'Faria'))