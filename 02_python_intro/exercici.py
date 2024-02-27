n1 = n2 = n3 = n4 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 +n2 + n3 + n4) / 4

print('sua media é {}' .format(media))

if (media >= 90):
    print('Muito bom, voce pode concorrer as maiores médias do colegio! dejesa concorrer a maior media ?')
    Resposta = input('Digite SIM ou NÃO para seguir em frente')
    if Resposta == 'SIM':
        print('Otimo, vamos dar continuidade... selecionarei os top 10 incluindo voce')
    if Resposta == 'NÃO':
        print('uma pena, fica pra proxima')
    else : print('Resposta invalida. tente novamente!')

if (media >=70):
    print('Voce está aprovado! Parabéns')
if (media >= 50):
    print('Voce precisa fazer uma recuperação')
    Resposta = input('Iniciar recuperação? SIM ou NÃO')
    if Resposta == 'SIM':
        print('Pergunta: Em qual ano aconteceu a revolução Russa ?')
        Resposta = input()
        if Resposta == ('1917'):
            print('Muito bom, Aluno. vou considerar uns pontos extras hehehe')
        else:
            print('Opá, parece que alguem não estudou')
    if Resposta == 'NÃO':
        print('É, parece qua alguém vai repetir de ano. não é mesmo guerreiro')
if (media < 50):
    print('VOCE FOI REPROVADO. ATÉ ANO QUE VEM!!!')







