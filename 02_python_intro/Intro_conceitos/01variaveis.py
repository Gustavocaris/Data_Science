# espaços de armazenamento na memória do computador que contêm valores. 
# Elas servem como "caixas" ou "recipientes" para armazenar dados que podem ser 
# manipulados e referenciados durante a execução de um programa.

name = 'Gustavo'
print(name)

media = 0
#variavel numeria não usa as aspas simples
n1 = n2 =n3 = n4 = 0.0
estado = True

# Função type ()
print(type(media))
print(type(n2))
print(type(name))
print(type(estado))

# Função isinstance ()
# -> vai retornar um valor verdadeiro se a variavel for do valor que voce determinou, do contrario é falso
a = 10
b = 'sol'
print(isinstance(a, float))
# pergunta: 'a variavel A é da classe float'
print(isinstance(a, (int, float)))
# pergunta: 'a variavel A é do tipo int ou do tipo float?'

#duas variaveis com dois valores diferentes
name, age = 'Gustavo', 23