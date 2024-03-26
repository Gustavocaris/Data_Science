# Problema: Encontrando o Anagrama
# Um anagrama é uma palavra ou frase formada pela reorganização das letras de outra palavra ou frase. 
# Por exemplo, "listen" é um anagrama de "silent". Neste exercício, você escreverá uma função em 
# Python para verificar se duas palavras são anagramas uma da outra.

# DESAFIO:
# Escreva uma função chamada sao_anagramas(palavra1, palavra2) que recebe duas strings como entrada 
# e retorna True se as duas palavras são anagramas uma da outra e False caso contrário.



def anagramas(palavra1, palavra2):
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()

    if len(palavra1) != len(palavra2):  # 'len' é para contar o tamanho da palavra;
       return False

    contagem1 = {}
    contagem2 = {}

    for letra in palavra1:
        contagem1[letra] = contagem1.get(letra, 0) + 1

    for letra in palavra2:
        contagem2[letra] = contagem2.get(letra, 0) + 1

    return contagem1 == contagem2

# Solicita ao usuário que insira as palavras
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Chama a função sao_anagramas com as palavras fornecidas pelo usuário e imprime o resultado
print(anagramas(palavra1, palavra2))

