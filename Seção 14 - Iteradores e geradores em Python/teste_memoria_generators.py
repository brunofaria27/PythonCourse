"""
Teste de memória com Generators

- Bom utilizar quando você quer um baixo consumo de memória
"""
# Função usando listas
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste fib_lista()
for n in fib_lista(1000):
    print(n)

# Função usando geradores
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste fib_gen()
for n in fib_gen(100000):
    print(n)
