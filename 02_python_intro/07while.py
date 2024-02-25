

# enquanto um numero for menor ou igual e a 10 faça
num = 1

#----------------------EXEMPLO-----------------
# while (num >= 100):
#     print(num)
#     num += 1
# print('Laço encerrado')


#----------------EXEMPLO---------------------

name = None

while True:
    print('Escreva seu nome, ou X para parar: ')
    name = input()
    if name == 'x' or name == 'X':
        break
    print(f'Bem vindo, {name} !')
print('Até logo!')