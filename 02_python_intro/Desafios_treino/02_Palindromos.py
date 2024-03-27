# Um palíndromo é uma palavra, frase, número ou outra sequência de caracteres que permanece a mesma 
# quando lida de trás para frente. Por exemplo, "radar", "bob", "12321" são palíndromos.

# ----DESAFIO ---

# Escreva uma função em Python chamada verificar_palindromo(palavra) que verifica se uma palavra é um palíndromo.
# Especificações:
# A função deve receber uma string palavra como entrada.
# A função deve retornar True se a palavra for um palíndromo e False caso contrário.
# A comparação deve ser case-insensitive, ou seja, "Bob" deve ser considerado um palíndromo, assim como "radar".

# Exemplo de entr e said:
# --->>> verificar_palindromo("python")
# False

palavra = input('digite uma palavra para verificarmos:  ')

def palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]  
    if palavra == palavra_invertida:  
        return True
    else:
        return False
    
resultado = palindromo(palavra)
print(resultado)

# -->>> verificar_palindromo("Bob")
# True

# -->>> verificar 'palavras' vamos usar o fatiamento de strings, que é: [inicio:fim:passo] 
