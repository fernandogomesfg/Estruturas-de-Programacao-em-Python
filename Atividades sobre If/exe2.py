# 3 - Crie um programa que fale sobre sua idade. As regras são as seguintes
# você deve receber por input sua idade, se você tiver ate três anos
# printe que é um bebe, ate 13 anos uma criança, ate 18 anos adolescente,
# até 65 adulto. Em nenhum deste casos é um idoso

idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <=3:
    print("Voce e um bebe")
elif idade >=4 and idade <=13:
    print("Voce e uma crianca")
elif idade >= 14 and idade <= 18:
    print("Voce e adolescente")
elif idade >= 19 and idade <= 65:
    print("Voce e adulto")
else:
    print("Voce e idoso")