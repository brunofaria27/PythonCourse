"""
Geradores

- São Iterators (Iteradores)
- O contrário não e verdadeiro

Outras informações:
- Geradores podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre funções e generator functions
-------------------------------------------------------------------------------------------------------------
/ Funções                                           / Generator Functions                                   /
-------------------------------------------------------------------------------------------------------------
/ utilizam return                                   / utilizam yield                                        /
-------------------------------------------------------------------------------------------------------------
/ retorna uma vez                                   / podem utilizar yield multiplas vezes                  /
-------------------------------------------------------------------------------------------------------------
/ quando executada retorna um valor                 / quando executada, retorna um generator                /
-------------------------------------------------------------------------------------------------------------
"""
# Exemplo função geradora
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
# OBS: Uma generator function não é um generator. Ela gera um generator

gen = conta_ate(10)
for num in gen:
    print(num)

gen2 = conta_ate(11)
print(next(gen2))
print('----------')
for num in gen2:
    print(num)

