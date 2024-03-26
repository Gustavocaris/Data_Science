import math

# Funções Trigonométricas
print("Seno de 45 graus:", math.sin(math.radians(45)))
print("Cosseno de 60 graus:", math.cos(math.radians(60)))
print("Tangente de 30 graus:", math.tan(math.radians(30)))
# funções trigonométricas esperam que os ângulos sejam fornecidos em radianos, 
# então usamos math.radians() para converter graus em radianos



# Funções Exponenciais e Logarítmicas
print("Exponencial de 2:", math.exp(2))
print("Logaritmo de 10 na base 2:", math.log(10, 2))
print("Logaritmo natural de 100:", math.log(100))

# Funções de Arredondamento
print("Teto de 4.3:", math.ceil(4.3))
print("Piso de 4.7:", math.floor(4.7))
print("Parte inteira de 5.9:", math.trunc(5.9))

# Constantes Matemáticas
print("Valor de pi:", math.pi)
print("Valor de e:", math.e)


#---Exemplooo_logaritmo;
x = 8 
y = 100

#   qual o logaritmo de Y na base 10 ?
logaritmo = math.log10(y)
print(logaritmo)

#mostrar o valor de PI
print(math.pi)







# Funções Builtin

Valores = [2, 4, 0, 10, 8, 11, 1]
print(min(Valores)) # mostrando o valor minimo e maximo
print(max(Valores))


# valor absoluto de 'a'
a = -5
b = 4
print(abs(a))

#Potenciação
print(pow(a,b)) # 'a' elevado a 'b'

# arredondar valores
c = 2.75165189
print(round(c,1))
