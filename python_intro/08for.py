# for item in sequencia: 
#       intruções executadas para cada item da sequencia
#       ou seja, um valor -> uma sequencia especifica pra ele


#----------------------EXEMPLO------------------
# lista = [2, 3, 4, 7, 1, 9, 10, 25, 32, 72, 23]

# for item in lista:
#     print(item)

#--------------------EXEMPLO-----------------
# lista = [2, 3, 4, 7, 1, 9, 10, 25, 32, 72, 23]
# palavra = 'Gustavo'
# for letra in palavra: # Perceba -> para cada letra uma palavra
#     print(letra)


# 'range' é uma função que gera uma sequência de números.
# pode usar o range para acessar elementos em uma lista ou em 
# outra estrutura de dados, usando os números gerados como índices
for numero in range(1,11):
    print(numero)

# Mostrar o nome na tela, exceto a pedra quartzo:

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)