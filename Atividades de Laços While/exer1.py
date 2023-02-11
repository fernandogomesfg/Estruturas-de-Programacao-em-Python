# 1 - Crie um programa que receba 5 números e retorne
# a média aritmética entre esses números

cont = 0
soma = 0
while (cont < 5):
    num = float(input("Digite um numero: "))
    soma = soma + num
    cont += 1
media = soma/5
print("O valor da media insida pelos numeros e de %.2f" %media)