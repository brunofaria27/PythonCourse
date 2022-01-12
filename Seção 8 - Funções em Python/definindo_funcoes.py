"""
Definindo Funções em Python
"""
# Exemplo de utilização de funções
cores = ['azul', 'preto', 'branco', 'vermelho']
# Utilizando a função integrada do Python print()
print(cores)
# Utilizando uma função que está dentro da lista
cores.append('roxo')
cores.clear() # Não recebe nenhum parametro
print(cores)

# Definindo funções
"""
def nome_da_funcao(parametro_da_funcao):
    bloco_da_funcao

- Parametros da entrada são opcionais
"""
def diz_oi():
    print("Olá!")

def cantar_parabens():
    print("Parabéns para você.")
    print("Nesta data querida,")
    print("Muitas felicidades")
    print("Muitos anos de vida!")
    print("AEEEEE !!!!")


# Chamando as funções criadas
diz_oi()
cantar_parabens()

# Podemos criar variavel do tipo função e executar a função através dessa variavel
canta = cantar_parabens
canta()