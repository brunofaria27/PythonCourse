"""
Debugando com PDB

COMANDOS:
l - listar onde estamos no código
n - próxima linha  
p - imprime variavel
c - continua a execução - finaliza debugging

- A partir do python3.7 não precisamos importar a biblioteca, pois a funcao 'breakpoint()' faz a mesma coisa
"""
# Exemplo PDB - Pyhton Debugger
# Precisamos importar a biblioteca PDB
# import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
nome_completo = nome + ' ' + sobrenome
# pdb.set_trace() # BreakPoint do PDB
breakpoint()
curso = 'Programação em Python Essencial.'
final = nome_completo + ' faz o curso ' + curso
print(final)