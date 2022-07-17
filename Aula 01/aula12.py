"""
len- Quantidade de caracter
aula 12
Não funciona com tipos numerios
"""
usuario = input('Digite o seu nome de usuário')
qtd = len(usuario)

if qtd < 6:
  print('ERRO')
else:
  print('OK!')

print(usuario, qtd, type(qtd))
string1 = input('Digite 1')
string2 = input('Digite 2')

(f'A quntidade de caracter foi {len(string1)+len(string2)}')
print(len(string2))
print(string2.__len__()) #Função len por de baixo dos panos
