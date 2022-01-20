"""
Escrevendo um iterador customizavel
"""
for n in range(0, 11):
    print(n)

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.maior
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)