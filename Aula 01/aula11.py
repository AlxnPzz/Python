"""
Operadores lógicos
and, or, not
in "Está" e not in "Não está"


#(Verdadeira E Verdadeira) = Verdadeiro
comparacao1 and comparacao2

#(Verdadeira E Falso) = Falso
comparacao1 and comparacao2

#Verdadeiro OU Verdadeiro = Verdadeiro
comp1 or com2

#Verdadeiro OU Falso = Verdadeiro
comp1 or com2
"""
a = 2
b = 3
if b>a:
    print("B e maior q A")
else:
    print("A é maior q B")

if not b>a:
    print("B e maior q A")
else:
    print("A é maior q B")
    
#=======================================
v1='asda'
v2=1

if not v2:
    print("Por favor, preencha o valor de A")
#=======================================
nome = 'Alexandre Piazza'
letra = input("Digite uma letra")

if letra not in nome:
    print(f'Existe a letra {letra} no seu nome')
else:
    print("Não existe essa letra")
#=======================================    
usuario = input('Nome do usuário')
senha = input('Senha do usuário')

usuario_db = 'Luiz'
senha_db = '123456'

if usuario_db == usuario and senha_db == senha:
  print('você está logado')
else:
  print('Invalido')
