"""
Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   
"""
idade = input("Digite sua idade: ")

if int(idade) >= 18:
     print("Você é maior de idade!")
elif int(idade) > 0  and int(idade) < 18:
    print("Você é menor de idade!")
else:
    print("Idade inválida")
   