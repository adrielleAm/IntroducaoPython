"""
Escreva um programa que ordene uma lista numérica com três elementos.
"""

lista = [5,7, 1]
#utilizando sort

#lista.sort()

print(lista)

#utilizando algoritimo

for i in range(len(lista)):
    menor = i
   
    for j in range(i +1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    
    if(lista[i] != lista[menor]):
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)
