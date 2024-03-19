# tupla é uma estrutura de dados semelhante a uma lista, mas com a diferença fundamental
# de que ela é imutável, ou seja, uma vez que uma tupla é criada, 
# seus elementos não podem ser modificados, adicionados ou removidos.

halogenios = ('F', 'Cl', 'Br', 'I')
gases_nobres = ('He', 'Ne', 'Ar')

elementos = halogenios + gases_nobres
print(elementos)


# quantas vezes aparece o numero 5 ?
t1 = (5, 5, 8, 9, 2, 5, 3, 4, 3, 6, 2)
print(t1.count(5))  
print(sum(t1))    # Pra somar todos os itens


# Opreações não disponiveis tupla : .sort() .append() .reverse()  .pop
# tudo que muda os itens, não é disponivel

for elemento in elementos:
    print(f'Elemento quimico: {elemento}')