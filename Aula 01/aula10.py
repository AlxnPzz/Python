"""
Operadores Relacionais
= - Você está afirmando algo
== - Você está perguntando se algo é igual a algo (Igualdade)
> - Maior que
>= - Maior que ou igual
< - Menor que
<= - Menor que ou igual
!= - Diferente de
"""
print(2 == 2)
print(2 == "1")

num_1 = 2
num_2 = 2
expressao = (num_1 >= num_2)

print(expressao)

print("====================================")
var_1 = 'Alexandre'
var_2= 'Piazza'
resultado = (var_1 != var_2)

print(resultado)

print("====================================")

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
#limites de idades
idade_min = 20 #muito jovem
idade_max = 40 #passou da idade

if idade >= idade_min and idade <= idade_max:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} NÃO PODE PEGAR')
