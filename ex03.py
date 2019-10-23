"""
Escreva um programa que resolva uma equação de segundo grau.  
"""

#a2 + bx + c
#(-b +- sqtr(b2-4ac))/2

from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4 * a * c

#Raiza de delta
raiz_delta = sqrt(delta)

#valor x1
x1 = (-b + raiz_delta) / (2 * a)

#valor x2
x2 = (-b - raiz_delta) / (2 * a)

print("x1 é igual a %f" %x1)
print("x2 é igual a %f" %x2)
