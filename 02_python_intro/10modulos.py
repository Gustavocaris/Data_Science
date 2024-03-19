# eu to dizendo pra importar do modulo math somente a funcionalidade para calcular raiz quadrada
from math import sqrt

# módulo é um arquivo contendo definições e declarações de Python. 
# O nome do arquivo é o nome do módulo com a extensão .py. Um módulo pode definir funções, 
# classes e variáveis, além de executar código quando é importado

# Para usar funcionalidades de um módulo em seu programa, você precisa importá-lo usando a instrução import.



import random

# Gerar um número inteiro aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)
print("Número aleatório:", numero_aleatorio)

# Escolher um elemento aleatório de uma lista
lista = ['a', 'b', 'c', 'd', 'e']
elemento_aleatorio = random.choice(lista)
print("Elemento aleatório da lista:", elemento_aleatorio)

#--------------------------------------------------------------------

import math

# Calcular o seno de um ângulo em radianos, operadores matematicos
angulo_radianos = math.pi / 4
seno = math.sin(angulo_radianos)
print("Seno de 45 graus:", seno)

# Calcular o logaritmo natural de 100
logaritmo = math.log(100)
print("Logaritmo natural de 100:", logaritmo)


#--------------------------------------------------------------------

import datetime

# Obter a data e hora atuais
agora = datetime.datetime.now()
print("Data e hora atuais:", agora)

# Formatar uma data
data_formatada = agora.strftime("%d/%m/%Y")
print("Data formatada:", data_formatada)

#----------------------------------------------------------------------

import os

# Obter o diretório de trabalho atual
diretorio_atual = os.getcwd()
print("Diretório de trabalho atual:", diretorio_atual)

# Listar arquivos em um diretório
arquivos = os.listdir()
print("Arquivos no diretório atual:", arquivos)

