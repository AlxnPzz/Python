"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

.lower # tudo minusculo
.upper # tudo maiusculo
.title # Primeiras letras maiusculas
"""
#:f - Número de ponto flutuante (float)
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f} é o resultado')

#:s - Texto (strings)

nome = "Alexandre"
print(f'{nome:s}')

#:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
v1 = 1
print(f'{v1:0>10}')
v2 = 15846
print(f'{v2:0^10}')
v3 = 15846
print(f'{v2:.2f}')
v4 = 15846
print(f'{v2:0>10.2f}')

nome2 = "alExandRE PiazZa dE LiMa fagUndES"
print(nome2.lower()) # tudo minusculo
print(nome2.upper()) # tudo maiusculo
print(nome2.title()) # Primeiras letras maiusculas
print(f'{nome2:#^50}')
