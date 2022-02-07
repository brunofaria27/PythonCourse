"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando o atributo __doc__ ou usando help()
"""
# Utilizando
def diz_oi():
    """Uma função simples que retorna a string 'oi'"""
    return 'oi'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou 'numero' à 'potencia' informada
    :param numero: Número que desejamos informar o exponencial
    :param potencia: Potência que desejamos gerar o exponencial. Por padrão e 2.
    :return: Retorna o exponencial do 'numero' por 'potencia'
    """
    return numero ** potencia


print(diz_oi.__doc__)
print(exponencial.__doc__)

# help(diz_oi)
# help(exponencial)