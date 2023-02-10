# 1 - Crie um programa que receba o seu saldo bancário e o quanto você deve.
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

saldo = int(input("Digite o seu saldo: "))
divida = int(input("Quanto voce deve? "))

saldoActual = saldo - divida
if (saldoActual > 0 ):
    print("Voce tem um saldo positivo!")
else:
    print("Voce tem um saldo negativo")

