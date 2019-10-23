#Strings
a = "Adrielle"
b = "Araujo"
nome = a + " " + b

print(nome)

#Tamanho de uma string
tamanho = len(nome)
print(tamanho)

#Índice
pos10 = nome[10]
print(pos10)

#sequencia [primeiro:ultimovalor]
seq = nome[1:6]
print(seq)

#Funções string
print(nome.lower())
print(nome.upper())

#remover espaço/caracter especial
nome = nome + "  " + "\n"
print(nome)
#Strip
print(nome.strip())

#converter uma string en uma lista
minha_string = "O rato roeu a ropa do rei de Roma"
minha_lista = minha_string.split(" ")
print(minha_lista)
minha_lista = minha_string.split("r")
print(minha_lista)

#Busca na string
busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

#Replace
print(minha_string.replace("o rei", "a rainha"))