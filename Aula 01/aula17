"""
While em Pyton
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores

while - enquanto
continue - continuar
break - finalizar
"""

v1 = 0
while v1 < 5:
    if v1 == 3:
        v1 = v1+ 1
        break
    print(v1)
    v1 = v1+1
print("Fim")

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'x vale {x} e Y vale {y}')
        y+= 1
    x += 1
print("Acabou")

# GERADOR DE TABUADA

x = input("Digite um numero")
y = 0
if x.isdigit():
    x=int(x)
    while y<=10:
        while y <= 10:
            print(f'{x} x {y} = {x*y}')
            y+=1
    print("Fim")
else:
    print("Valor invalido")

print("Digite um valor, caso queira gerar a tabuada escreva 'Tabuada'")
num1 = input("Digite um numero ")
op = input("Digite o operador ")
num2 = input("Digite outro numero ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        print(f'O valor é {num1+num2}')

    elif op == '-':
        print(f'O subtração é {num1-num2}')
    elif op == '/':
        print(f'O divisão é {num1/num2:.2f}')
    elif op == '*':
        print(f'A multiplicação é {num1*num2}')
    elif op == 'Tabuada':
        op1 = 0
        while op1 <= 10:
            print(f'{num1} x {op1} = {num1*op1}')
            op1 +=1
    else:
        print('Operador não encontrado')
else:
    print("Valor inválido")
