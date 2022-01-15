"""
Módulo random e o que são módulos?

Módulos -> outros arquivos em python
Módulo random -> várias funções para geração de números pseudo-aleatórios
"""
# Importar módulo inteiro
import random

# Vendo todas as funcoes disponiveis
print(dir(random))

# Funções:
# Lembrando devemos colocar random.'funcao', porque as funções vem da classe random, como se fosse em Java
# random() -> gera um número aleatorio entre 0 e 1
# uniform(number1, number2) -> gera um número aleatório entre os number1 e number2
# randint(number1, number2) -> gera valores aleatórios inteiros, entre os valores number1 e number2
# choice() -> mostra um valor aleatório entre um iteravel
# shuffle() -> Tem a função de embaralhar os dados