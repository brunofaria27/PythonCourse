"""
Sistema de arquivos manipulação
"""
# Imports
import os

# Descobrindo se um arquivo ou diretório existe
# Arquivo
print(os.path.exists('arquivo_exercicio.txt'))
print(os.path.exists('arquivo.txt'))
# Diretório
print(os.path.exists('geek'))
print(os.path.exists('selecao'))

# Criando arquivos
# Forma 1:
open('arquivo_teste.txt', 'w').close()
# Forma 2:
open('arquivo_teste2.txt', 'a').close()
# Forma 3:
with open('arquivo_teste3.txt','w') as arquivo:
    pass # Não faz nada no bloco -> coloca pass
# Forma 4 (Melhor forma de criar):
os.mknod('arquivo_teste4.txt')
os.mknod('home/geek/arquivo_teste5.txt')

# Criando diretórios únicos -> um a um
os.mkdir('templates')
os.mkdir('templates/geek')

# Criando multi diretorios
os.makedirs('bruno/rodrigues/faria/teste/multi/diretorios', exist_ok=True) # exist_ok=True -> ele ignora se existir e não da erro

# Renomear diretórios e arquivos
# Diretórios
os.rename('geek2/novo2', 'geek2')
# Arquivos
os.rename('frutas.txt', 'cesta.txt')

# Deletar arquivo ou diretório
# OBS: Preste atenção, porque os itens excluídos não vão para a lixeira
# Removendo arquivos
os.remove('geek.txt')
# Removendo diretórios
os.rmdir('templates') # Se ele tiver conteúdo terá um erro

# Removendo uma árvore de diretórios
for arquivo in os.scandir('geek2'):
    print(f' - {arquivo.name}')
    if(arquivo.is_file()):
        os.remove(arquivo.path)

# Trabalhando com arquivos e diretorios temporarios
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei diretory temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'teste\n') # Em arquivos temporários so conseguimos escrever bits, por isso utilizamos o b''
    tmp.seek(0)
    print(tmp.read())

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'nome do bruno')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()
