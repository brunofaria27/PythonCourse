"""
Levantando os próprios erros com raise

OBS: raise não é uma função, mas sim uma palavra reservada.
- raise ascende ("executa") uma exceção quando é chamado -> ótimo para tratamento de erros
- Nada é executado depois do raise
"""
# Exemplo real:
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('TEXTO PRECISA SER UMA STRING.')
    if type(cor) is not str:
        raise TypeError('COR PRECISA SER UMA STRING.')
    print(f'O texto {texto} será impresso na cor {cor}.')

# colore(1, 'banana')
colore('Oi Bruno', 'azul')
