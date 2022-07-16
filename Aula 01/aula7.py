'''
Formatação de string
'''
nome = 'Alexandre'
idade = 19
altura = 1.86
e_maior = idade > 18
peso = 76
imc = peso/(altura**2)

print("O IMC da pessoa é", peso/(altura*altura),"Nome é", nome)
print(f'{nome}, seja bem vindo ao código,{idade}, logo você é {e_maior}, maior de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e seu peso é{} e seu IMC é de {:.2f}'.format(nome,idade,peso,imc))

#      0       1                            2                   3      |     0     1     2   3
print('{0} tem {1} anos de idade e seu peso é{1} e seu IMC é de {3:.2f}, seu nome é {0}'.format(nome,idade,peso,imc))
#:.2f - Para delimitar a quanidade de casas decimais.