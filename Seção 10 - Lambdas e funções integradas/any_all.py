"""
Any e All

all() -> Retorna true se todos os elementos sao verdadeiros ou o iteravel e vazio
any() -> Retorna true se qualquer elemento do iteravel for true, se o iteravel estiver vazio retorna true
"""
# Utilizando o all()
nomes = ['Bruno', 'Bernardo', 'Beatriz', 'Nati']
print(all([nome[0] == 'B' for nome in nomes]))

# Utilizando o any
print(any([nome[0] == 'N' for nome in nomes]))