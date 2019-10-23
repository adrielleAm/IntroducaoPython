meudicionario = {"A": "ameixa", "B": "banana", "C": "coco", "D":"Damasco" }

print(meudicionario)
print(meudicionario["A"])
print(meudicionario["B"])
print(meudicionario["C"])

for chave in meudicionario:
    print(chave+": " + meudicionario[chave])

for i in meudicionario.keys():
    print("Chave: " + i)

for i in meudicionario.values():
    print("Valor: " + i)