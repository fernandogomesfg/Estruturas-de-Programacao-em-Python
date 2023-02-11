# 2 - Crie um programa que receba 5 números, realiza a soma destes números,
# mas caso um destes números seja negativo não considere ele na soma.
from builtins import input

cont = 0
soma = 0

while (cont < 5):
    num = float(input("Digite um numero: "))
    if (num > 0):
        soma = soma + num
    cont += 1

print("A soma dos numeros positos inseridos e: %.2f " %soma)