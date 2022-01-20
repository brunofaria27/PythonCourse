"""
Decoradores com diferentes assinaturas
"""
# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

# @gritar Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando
print(saudacao('Angelina'))
print(ordenar('picanha', 'batata frita'))

# Refatorando com Decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando Decorator Pattern
print(saudacao('Felicity'))
print(ordenar('picanha', 'batata frita'))

# Decorator com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# Testando
print(soma_dez(10, 12))
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('sanduiche', 'pizza'))
