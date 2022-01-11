"""
Módulos Collections - Deque

Deque -> Lista de alta performace
"""
from collections import deque

# Criando deque
deq = deque('Geek')
print(deq)

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
deq.appendleft('J') # Adiciona no inicio

# Removendo elementos no deque
print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq.popleft()) # Remove e retorna o primeiro elemento