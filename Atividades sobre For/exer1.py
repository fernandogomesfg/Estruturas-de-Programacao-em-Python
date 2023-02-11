# 1 - Crie um programa que receba uma string por input e conte quantos
# caracteres ela têm, não leve em conta caracteres de espaço.
# Você não deve usar o len().

cont =0
texto = input("Digite uma string: ")
for x in texto:
    if x != " ":
        cont = cont +1
print("A string tem %d caracteres" %cont)