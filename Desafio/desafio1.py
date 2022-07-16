"""

Criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibir um texto com os valores na tela usando F-Strings (com as chaves)
"""
nome ='Alexandre'
idade = 18
altura = 1.86
peso = 86.0
ano_atual = 2022
imc = peso/(altura**2)

print(f'Alexandre tem {idade} com altura {altura} e pesa {peso}, o seu IMC é de{imc}, e também {nome}, nasceu em {ano_atual-idade}')
print('{n} tem {id} com a altura {a} e pesa {p}, \no seu IMC é de {i}, e tambem {n}, \nnasceu em {aa}'.format(n=nome,id=idade,a=altura,p=peso,i=imc,aa=idade-ano_atual))