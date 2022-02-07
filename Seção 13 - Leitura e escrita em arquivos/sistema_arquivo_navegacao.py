"""
Sistema de arquico e navegação
"""
# Imports
import os

# getcwd() -> pega o current work directory - diretorio de trabalho recorrente
# retorno o path = caminho absoluto
print(os.getcwd())

# para mudar o diretório podemos usar chdir()
os.chdir('..') # volta uma pasta

# podemos checar se o path (caminho) para um diretório é relativo ou absoluto -> os.path.isabs('directory')
# podemos indentificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# podemos ter mais detalhes do sistema operacional
print(os.uname())