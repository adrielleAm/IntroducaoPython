# coding: utf-8 
#LER ARQUIVO
"""
    arquivo = open("arquivo.txt")

    linhas = arquivo.readlines()
    texto_completo = arquivo.read()

    print(texto_completo)
"""
#CRIAR ARQUIVO (APAGA CASO JÁ EXIXTA)
"""
    w = open("arquivo2.txt", "w")
    w.write("Esse é o meu arquivo ")
    w.close()
"""
#EDITAR ARQUIVO
a = open("arquivo2.txt", "a")
a.write("\nLinha 2")
a.close()
