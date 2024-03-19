# numeros aleatorios, 'random' pra gerar os N aleatorios 

import random

# --------EXEMPLO ----- gerando um numero aleatorio entre 1 e 20
# valor = random.randint(1,20)
# print(valor)

# -----------EXEMPLO-----------gerando cincp numeros aleatorios
# print('gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')


#-----------EXEMPLO----------Numeros flutuantes
valor = random.random()
print(f'Número gerado: {round(valor * 10, 2)}') # 'round' para arredondar o valor para até duas casas decimais 


# ------------EXEMPLO------------escolher um valor dentro de uma lista
L = [2, 4, 6, 8, 15, 17, 19, 23, 25, 39, 51]
n = random.choice(L)
print(f'Número escolhido: {n}')

#---pra escolher varios valores eu utilizaria o 'random.sample'