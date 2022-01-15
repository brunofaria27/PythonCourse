"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura não podemos escrever nele, apenas ler, vice-versa.
- Se o arquivo não existir ele será criado.
- Caso ele já exista todo o conteúdo do arquivo será apagado e outro será criado.
"""
# Exemplo:
with open('arquivo_teste_escrita.txt', 'w') as arquivo:
    arquivo.write('Bruno Faria.\n')
    arquivo.write('21 anos.\n')
    arquivo.write('Estudante de Ciências da Computação.')

# Modo não Pythonico de escrever em arquivos
arquivo = open('arquivo_teste_escrita2.txt', 'w')
arquivo.write('Um texto qualquer\n')
arquivo.write('última linha do arquivo')
arquivo.close()

# Exemplo menos simples:
with open('arquivo_exercicio.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
