"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se ese número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
numero1 = input("Digie o seu numero")

if numero1.isdigit():
    numero1=int(numero1)
    if numero1%2==0:
        print("O numero é par")
    else:
        print("O numero é impar")
else:
    print("O valor é inválido?")

# Mesmo código em ordem invertida

numero2 = input("Digite outro numero")

if not numero2.isdigit():
    print("Esse é um valor inválido")
else:
    numero2 = int(numero2)
    if not numero2 %2 == 0:
        print("É impar")
    else:
        print("É par")