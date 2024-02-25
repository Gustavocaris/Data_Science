import random       #importa o módulo random, que fornece funções para gerar números aleatórios.

for A in range(1,6):                #Em cada iteração, A recebe o valor do próximo número no intervalo (1, 2, 3, 4, 5).
    print(f'\nConjunto {A}')        #esta linha imprime o título do conjunto, que consiste na palavra "Conjunto" seguida pelo valor atual de A.
    for B in range(5):              #Dentro do loop for aninhado, outro loop for é criado.
        num = random.randint(1,100) #Dentro do loop aninhado, esta linha gera um número aleatório inteiro no intervalo de 1 a 100 (inclusive) e o armazena na variável num
        print(f'valor : {num}')     #esta linha imprime o valor aleatório gerado na iteração atual do loop, utilizando uma f-string para formatar a saída.

#-----------------RESUMO----------------
# Resumindo, este código gera conjuntos de valores aleatórios, 
# cada conjunto contendo 5 valores aleatórios no intervalo de 1 a 100. 
# O código imprime cada conjunto com um título indicando o número do conjunto.