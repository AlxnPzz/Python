"""
Tipos de dados
str- string - 'Assim' ou "Assim"
int- inteiro - 0 - 10 - 20 - 50 - 1000
float - real/ponto flutuante -10.50 - 1.5 --10.10 - -50.93  0.0 - Numero com casas decimais
bool- boleano/lógico - True/False 10==10
"""

print('Alexandre',type("Alexandre"))
print(10,type("10"))
print(25.26,type("25.26"))
print(10==10,type(10==10))
print('L'=='L',type('L'=='L'))
"""
Type retorna o tipo do calor
"""
print('Alexandre',type('Alexandre'),bool('Alexandre'))
print('10',type('10'), type(int('10')))
"""
Qualquer valor convertido para Boleano ela avalia como verdadeiro
"""
#Str: nome
print('Alexandre',type('Alexandre'))

#Idade: int
print('18',type(18))

#Altura: float
print('1.87',type(1.87))

#Boleado >= maior
print(19 > 18,type(19 > 18))