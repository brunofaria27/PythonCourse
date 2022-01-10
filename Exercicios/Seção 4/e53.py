# Entrada de dados
comprimento_terreno = int(input("Digite o comprimento do terreno: "))
largura_terreno = int(input("Digite a largura do terreno: "))
preco_tela = int(input("Digite o valor do metro da tela: "))

# Processamento
area = comprimento_terreno * largura_terreno
preco_total = preco_tela * area

# Saída de dados
print(f'O valor para colocar a tela na area toda é de R${preco_total}')
