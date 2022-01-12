"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a propriedade especial __doc__
help.__doc__ -> Exemplo
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