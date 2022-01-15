"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package
Você pode conhecer todos os pacotes externos oficiais em: pypi.org

colorama -> E utilizado para permitir a impressão de textos coloridos no terminal
"""
# Importando colorama
from colorama import init, Fore

# Utilizando
init()
print(Fore.BLUE + 'Oi, meu nome é Bruno!')
print(Fore.MAGENTA + 'Estou estudando Python em minha casa...')

# Outro módulo Externo
import pydf

pdf = pydf.generate_pdf('<h1>Título criado pelo Pyhton! </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)