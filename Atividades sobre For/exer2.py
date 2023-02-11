# 2 - Crie um programa que faça o calculo do fatorial de um número.
# O fatorial a ser calculado deve ser recebido por input.

fat = 1
num = int(input("Digite um numero: "))

for num in range (num,1,-1):
    fat = fat * num
print("Factorial de %d e igual a %d" %(num, fat))