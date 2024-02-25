# Crie um script que peça para o usuario digitar o nome de 5 bebidas favoritas
# e armazenar esses valores em uma lista, na sequencia, exibindo na tela os elementos 
# da lista em ordem alfabetica, um por linha;

bebidas = []

for i in range(5):
    print('Digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()   #sort -> para classificar e deixar em ordem crescente

print(f'\nbebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

print(f'\saude!')