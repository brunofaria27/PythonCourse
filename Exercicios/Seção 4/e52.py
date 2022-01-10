# Entrada de dados
print("Insira o valor investido pelos três amigos: ")
investimento_amigo1 = int(input())
investimento_amigo2 = int(input())
investimento_amigo3 = int(input())

print("Insira o valor do prêmio da loteria: ")
valor_premio = int(input())

# Processamento
relacionamento = valor_premio / (investimento_amigo1 + investimento_amigo2 + investimento_amigo3)
recebimento_amigo1 = investimento_amigo1 * relacionamento
recebimento_amigo2 = investimento_amigo2 * relacionamento
recebimento_amigo3 = investimento_amigo3 * relacionamento

# Saída de dados
print(f'Os amigos receberiam, respectivamente: \n Amigo 1: {recebimento_amigo1} \n Amigo 2: {recebimento_amigo2} \n Amigo 3: {recebimento_amigo3}')