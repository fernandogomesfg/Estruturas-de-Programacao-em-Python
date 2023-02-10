# 4 - Crie um programa que receba dois números, e também receba do usuário
# a operação que deve ser feita, as possibilidades são soma(+), subtração (-),
# divisão(/) e multiplicação(*).
# Realize a operação escolhida sobre os dois números.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
oper = input("Escolha uma operacao: ")

if oper == "+":
    res = num1 + num2
    print("%.2f + %.2f = %.2f " %(num1, num2, res))
elif oper == "-":
    res = num1 - num2
    print("%.2f - %.2f = %.2f " % (num1, num2, res))
elif oper == "*":
    res = num1 * num2
    print("%.2f * %.2f = %.2f " % (num1, num2, res))
elif oper == "/":
    res = num1 / num2
    print("%.2f / %.2f = %.2f " % (num1, num2, res))
else:
    print("Opcao invalida")