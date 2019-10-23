"""
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.  
"""

def soma(a, b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
      return  a / b

a = int(input("Digite o primeiro numero: "))
op = input("Digite o operador: ")
b = int(input("Digite o segundo numero: "))

try:
    if op == "+":
        resultado = soma(a,b)
    elif op == "-":
        resultado = subtracao(a,b)
    elif op == "/":
        resultado = divisao(a, b)
    elif op == "*":
        resultado = multiplicacao(a,b)

    print(resultado)
except:
    print("Não foi possivel realizar a operação!")


    