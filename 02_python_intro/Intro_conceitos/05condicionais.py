# IF , ELIF , ELSE

# Pode ser : simples, composto, encadeado 

n1 = n2 = 0.0
media = 0.0

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = (n1 +n2) / 2

print('sua media é {}' .format(media))

if (media >= 70):
    print('Parabéns, voce foi Aprovado')
if (media >=50):  #poderia usar um 'ELIF' PARA REALIZAR OUTRO TESTE TAMBEM
    print(' Voce está de recuperação')
else:
    print('Aluno Reprovado')