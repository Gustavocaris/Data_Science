# exercicio

# Escreva um programa Python que calcula o fatorial de um número inteiro não negativo dado pelo usuário.

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        conta = ' x '.join(str(i) for i in range(2, numero + 1))
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial, conta
    
numero = int(input('Digite um numero aqui inteiro e não negativo:  '))

if numero < 0:
    print('Digite um numero inteiro e positivo!!')
else :
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")

# COMENTARIO DA LINHA 10 (foi a partir mais complicadinha que eu achei)

# cria uma representação da conta que será feita para calcular o fatorial. 
# A expressão range(2, numero + 1) cria uma sequência de números de 2 até 
# o número fornecido, e str(i) for i in ... transforma cada número dessa 
# sequência em uma string. join() então junta essas strings usando o 
# texto " x " como separador. Por exemplo, se numero for 5, a variável 
# conta será "2 x 3 x 4 x 5".
