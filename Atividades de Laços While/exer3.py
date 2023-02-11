# 3 - Cria um programa que receba um número arbitrário (definido pelo usuário)
# de números que serão lidos e retorne a soma de todos eles.

cont = 0
soma = 0
qtd = int(input("Digite a quantidade de vezes que o programa deve rodar: "))

while (cont < qtd):
    num = float(input("Digite um numero: "))
    soma = soma + num
    cont += 1
print("A soma dos valores inseridos pelo teclado e: %.2f" %soma)