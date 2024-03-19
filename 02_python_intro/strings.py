# string é uma sequência de caracteres. 
# Ela pode conter letras, números, símbolos e espaços. 
# As strings são imutáveis, o que significa que, uma vez criadas, elas não podem ser modificadas.

# Criando uma string
minha_string = "Olá, mundo!"

# Imprimindo a string
print(minha_string)

# Acessando caracteres individuais da string
primeiro_caractere = minha_string[0]
print("O primeiro caractere é:", primeiro_caractere)

# Concatenando strings
outra_string = " Esta é outra string."
concatenada = minha_string + outra_string
print("String concatenada:", concatenada)

# Tamanho da string (número de caracteres)
tamanho = len(concatenada)
print("Tamanho da string concatenada:", tamanho)

# Iterando sobre uma string
for caractere in minha_string:
    print(caractere)
