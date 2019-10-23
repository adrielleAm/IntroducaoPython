# Textos
"""
    print("Ola mundo!")
"""
# Operações Matemáticas
"""
    print(10 / 3)
    print(10 % 3)
    print(2+2)
    print(2**2)
"""

# Variáveis
"""
    minha_variavel = "Olá mundo"
    print(minha_variavel)
"""

#Tipos de dados
"""
    var1 = 1 #variável inteira
    var2 = 1.1 #variável float
    var3 = "Eu sou uma string"  #variável string
    var4 = True #variavel boolean true or false

    print(var1)
"""
#Operadores relacionais
"""
    x = 2
    y = 3
    soma = x + y

    print(soma > 10)
"""
#Operadores Lógicos
"""
    x = 2
    y = 3
    z = 4

    print(x == y and x != z)
    print(x == y or x != z)
    print(x == y or x == z and z == y)
"""
#Comandos condicionais if
"""
    x = 1
    y = 100000
    if x > y:    
        print("x é maior que y")
    if y > x:
        print("y é maior que x")
"""

#Comando condicional else
"""
    x = 1
    y = 2
    if x > y:
        print("x é maior que y")
    else:
        print("x não é maior que y")
    
    #Parte 2
    if x == y:
        print("numeros iguais")
    elif x < y:
        print("x menor que")
    elif y > x:
        print("y maior que x")
"""
#Laços de repetição
#while
"""
x = 1
while x < 10:
    print(x)
    x += 1
"""
#for
"""
lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]

for i in lista2:
    print(i)
"""
#for range (cria uma lista)
"""
for i in range(10,20,2):
    print(i)
"""
#input
"""
numero = input("Digite um numero: ")
print("O número digitado é:")
print(numero)
"""
nome = input("Digite seu nome: ")
print("Bem vindo " + nome)