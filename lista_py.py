minha_lista = ["abacaxi", "maça", "abacate", "pera"]
minha_lista_2 = [1,2,3,4,5,6]
print(minha_lista)
print(minha_lista_2)

#Índice Lista
print(minha_lista[2])
print(minha_lista_2[2])

#Loop Lista
for item in minha_lista:
    print(item)

#Tamnho lista
print("Tamanho")
print(len(minha_lista))

#Adicionando 
minha_lista.append("limão")
print(minha_lista)

#buscar elemento na lista 
if 3 in minha_lista_2:
    print("3 está na lista")

#Removendo elementos
del minha_lista[2:3]
print(minha_lista)

#Ordenar lista 
print("==========PARTE 2 ==========")
lista = [124,256,75,58,6,4,5,6]

#ORDENA CRESCENTE
lista.sort()
print(lista)
#ORDENA DECRESCENTE
lista.sort(reverse=True)
print(lista)

#INVERTE A LISTA
lista2 = [124,256,75,58,6,4,5,6]
lista2.reverse()
print(lista2)

lista_txt = ["bola", "faca", "dinheiro"]
lista_txt.sort()
print(lista_txt)