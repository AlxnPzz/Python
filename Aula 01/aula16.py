"""
Índice e fatiamento de strings

Manipulando strings
* String indices
* Fatiamento de strings (incio:fim:passo)
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Tipos de built-in https://docs.python.org/3/library/stdtypes.html
Funções bluit-in https://docs.python.org/3/library/functions.html
"""

#       [012345678] - Positivos
texto = 'Python_s2'
#      -[987654321] - Negativos
print(texto[8])

novastring = texto[2:6]
print(novastring)

novastring2 = texto[:6] # Pegar apartir do 0
print(novastring2)#[-1] pega o ultimo caracter

novastring3 = texto[7:] # Pegar até o final da string
print(novastring3)

novastring4 = texto[0::3] # Dando o passo de pulo
print(novastring4)

#============================

print(len(texto))
