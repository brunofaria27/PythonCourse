"""
**kwargs

- Este é so mais um parametro, mas diferente do *args, o **kwargs exige que utilizemos parametros nomeados, e tranforma esses parametros extras em dicionario.
OBS: Os parametros *args e *kwargs não são obrigatórios
"""
# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')

cores_favoritas(marcos='verde', juliana='azul', bruno='preto')

# Exemplo mais complexo
def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um comprimento do Python.'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é!'

print(comprimento_especial())
print(comprimento_especial(geek='Python'))
print(comprimento_especial(geek='Oi'))
print(comprimento_especial(geek='especial'))

