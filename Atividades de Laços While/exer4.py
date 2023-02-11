# 4 - Percorra os números de 2 até 10 e diga se o número é par ou impar.

cont = 2
while(cont <= 10):
    if (cont % 2 == 0):
        print("O numero %d e par" %cont)
    else:
        print("O numero %d e impar" %cont)
    cont += 1