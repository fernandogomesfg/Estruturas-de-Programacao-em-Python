# 2 - Crie um programa que possui uma variável que guarde seu CPF e que guarde
# uma senha de sua escolha. Em seguida receba por input uma senha do usuário.
# Caso a senha recebida seja a correta mostre o CPF,
# caso não diga que a senha esta incorreta.
from tkinter import _setit

CPF = "123-123-123-45"
senha = "fernando"

senhaInput = input("Digite sua senha: ")

if (senhaInput == senha):
    print("O seu CPF e: " ,CPF)
else:
    print("A senha esta incorrecta")