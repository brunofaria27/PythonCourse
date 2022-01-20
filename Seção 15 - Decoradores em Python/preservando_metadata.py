"""
Preservando Metadata

Metadados -> São dados intrísecos em arquivos.
wraps -> São funções que envolvem elementos com diversas finalidades.
"""
# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b

print(f'Problema sem ser solucionado: ')
print(soma.__name__)
print(soma.__doc__)

# Resolução do problema 
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b

print(f'Resolução do problema: ')
print(soma(10, 20))

print(soma.__name__)
print(soma.__doc__)
print(help(soma))