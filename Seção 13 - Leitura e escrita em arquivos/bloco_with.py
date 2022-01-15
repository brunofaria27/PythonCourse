"""
Bloco With

- O bloco with é utilizado para criar um contexto de trabalho onde os recursos de trabalho são fechados após o bloco with.
- O próprio bloco with abre e fecha o arquivo para a gente.
"""
# Utilizando o bloco - forma pythonica de manipular arquivos
with open('arquivo_para_testes.txt') as arquivo:
    print(arquivo.readlines())

print(arquivo.read())