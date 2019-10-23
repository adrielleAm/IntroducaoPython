from functools import reduce


x = [1,2,3,4,5]
y = []

#Utilizando for
for i in x:
    y.append(i**2)

print(x)
print(y)

#Ultilizando list Comprehension
x = [2,4,6,8,10, 9]
y = [i**2 for i in x]
z = [i for i in x if i %2 == 1]
print("===")
print(x)
print(y)
print(z)

print("===== ENUMERATE =====")
lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
    print(i, nome)

print("===== FILTER =====")

def pares(i):
    if i % 2 == 0:
        return i

lista2 = [1,2,3,4,5,6,7,8,9]
lista_pares = filter(pares, lista2)

print(list(lista_pares))

print("===== MAP =====")

def dobro(x):
    return 2*x

lista3 = [1,2,3,4,5,6]
lista_dobro = map(dobro, lista3)
print(list(lista_dobro))

print("===== REDUCE =====")

def soma(x, y):
        return x + y

lista4 = [1,2,3,5,8,20]

soma = reduce(soma, lista4)

print(soma)

print("===== ZIP =====")

lista5 = [1,2,3]
lista6 = ["abacate", "faca", "dado"]

for numero, nome in zip(lista5, lista6):
    print(numero, nome)