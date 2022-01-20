"""
Decoradores (Decorators)

- São funções
- Envolvem outras funções e aprimoram seus comportamentos
- São exemplos de HOF
- Tem uma sintaxe própria , usando '@' (Syntact Sugar)

---------------------------------------------------------------------
|                       Function Decorator                          |
---------------------------------------------------------------------

---------------------------------------------------------------------
|       -----------------------------------------------------       |
|       |                  Função Decorada                  |       |
|       -----------------------------------------------------       |
---------------------------------------------------------------------
"""
# Decorators como funções (Sintaxe não recomendada / Sem açucar sintático)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um ótimo dia.')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 1:
teste = seja_educado(saudacao)
teste()

# Testando 2:
def raiva():
    print('EU TE ODEIO.')

raiva_educada = seja_educado(raiva)
raiva_educada()

# Decorators como Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você.')
        funcao()
        print('Tenha um ótimo dia.')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Bruno')

@seja_educado_mesmo
def dormir():
    print('Quero muito dormir...')

# Testando
apresentando()
dormir()