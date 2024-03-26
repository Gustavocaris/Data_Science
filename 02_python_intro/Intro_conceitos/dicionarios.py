# dicionário é uma estrutura de dados poderosa e flexível que permite armazenar pares de chave-valor. 
# Cada valor é associado a uma chave única, e isso permite acessar e manipular os valores através das chaves, 
# em oposição aos índices numéricos usados em listas.

meu_dicionario = {
    'chave1': 'valor1', 
    'chave2': 'valor2', 
    'chave3': 'valor3'
    }

print(meu_dicionario['chave1'])  # imprimir 'valor1'

# ---> Adição e Modificação de Valores
meu_dicionario['nova_chave'] = 'novo_valor'  # Adicionando um novo par chave-valor
meu_dicionario['chave1'] = 'novo_valor1'  # Modificando o valor associado a uma chave existente

# ---> Remoção de Pares Chave-Valor
del meu_dicionario['chave1']  # Isso removerá o par chave-valor associado à chave 'chave1'


# ---> Verificação de Existência de Chaves
if 'chave1' in meu_dicionario:
    print("A chave 'chave1' existe no dicionário.")


# ---> Iteração
for chave, valor in meu_dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
