"""
Map - Mapeamento de valores para função
"""
import math

def area(r):
    return math.pi * (r ** 2)
print(area(2))

# Forma comum
raios = [2, 5, 7.1, 8.3, 10, 44]
areas = []
for r in raios:
    areas.append(area(r))
print(area)

# Forma com map
areas = map(area, raios)
print(areas)

# Forma map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

