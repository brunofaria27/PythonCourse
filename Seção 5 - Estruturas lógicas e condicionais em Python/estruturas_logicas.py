"""
Estruturas Lógicas

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para 'and' ambos os valores precisam ser verdadeiros
Para 'or' ou um ou outro precisa ser verdadeiro
Para 'is' é usado para comparação (ativo is True)
"""
ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário ")
else:
    print("Você precisa ativar sua conta, cheque seu e-mail antes.")