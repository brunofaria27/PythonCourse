"""
Dicionários - Lembra um JSON

OBS: Em algumas linguagens de programação dicionarios em Python são conhecidos por mapas.
- Dicionários são coleções do tipo chave/valor.
- Dicionários são representados por chaves {}.

OBS: Sobre dicionários:
    - Chaves e valor são separados por dois pontos 'chave:valor';
    - Tanto a chave quanto o valor pode ser de qualquer tipo de dado;
    - Podemos misturar tipo de dados;
"""
# Criação de dicionários
# Forma 1 (Mais comum):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'}
print(paises)
print(type(paises))
# Forma 2 (Menos comum):
paises2 = dict(br='Brasil', eua='Estados Unidos', pt='Portugal')
print(paises2)
print(type(paises2))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que em lista/tupla
"""
OBS: Caso tentamos acessar uma chave que não exite = KeyErro
"""
print(paises['br'])
print(paises['pt'])
# Forma 2 - Acessando via get (Recomendado)
"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio, porém, falar que é um tipo sem tipo é mais apropriado.
OBS: O tipo None é sempre especificado com a primeira letra maiuscula.

Quando utilizamos?
- Podemos utilizar o None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de recebermos um valor final.

OBS: O tipo None em Python é sempre considerado como Falso.
"""
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('ru')) # Retorna None -> não acontece o KeyError

# Encontrando um pais utilizando get
# Forma 1:
pais = paises.get('br')
if pais:
    print(f'Encontrei o {pais}.')
else: 
    print(f'Não encontrei o pais desejado.')
# Forma 2:
# Definir um valor padrão para caso não encontremos um objeto com a chave informada.
pais1 = paises.get('ru', 'Não encontrado')
print(f'Encontrei o país {pais1}')

# Ver se determinada chave se encontra no dicionario
print('br' in paises)
print('ru' in paises)
print('pt' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utlizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla dicionário, como chaves de dicionários.
localidades = {
    (13.999, 12.012): 'Escritório em Belo Horizonte',
    (34.919, 12.933): 'Escritório em São Paulo',
    (123.999, 31.982): 'Escritório em New York'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
"""
Conclusão 1: a forma de atualizar e adicionar dados no dicionário é a mesma.
Conclusão 2: em dicionário não podemos ter chaves repetidos (sobrescrever valores dos dados).
"""
receita = {'jan':120, 'fev':232, 'mar':92}
print(receita)
# Forma 1 (Mais comum):
receita['abr'] = 350
print(receita)
# Forma 2 (Menos comum):
novo_dado = {'mai':450}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário
"""
Conclusão 1: a forma de atualizar e adicionar dados no dicionário é a mesma.
Conclusão 2: em dicionário não podemos ter chaves repetidos (sobrescrever valores dos dados).
"""
# Forma 1:
receita['mai'] = 550
print(receita)
# Forma 2:
receita.update({'mai':600})
print(receita)

# Remover dados de um dicionário
# Forma 1:
"""
OBS: Ao removermos um objeto, o valor deste objeto e sempre retornado.
"""
receita.pop('mar') # Sempre precisamos informar a chave -> KeyError se não achar
print(receita)
# Forma 2:
"""
OBS: Se a chave não existir será retornado um KeyError, e também neste caso o valor removido não é retornado.
"""
del receita['fev']
print(receita)

# Metódos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
# Limpar dicionário
# d.clear()

# Copiando um dicionário para o outro
# Forma 1 (Deep Copy):
novo = d.copy
print(novo)
# novo['d'] = 4
print(d)
print(novo)
# Forma 2 (Shallow Copy):
novo = d
print(novo)
# novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários
"""
O metódo fromkeys recebe dois parâmetros: um interavel e um valor, ele irá gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
"""
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)