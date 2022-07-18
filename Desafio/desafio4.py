"""
Faça um progrmaa que peça o primeiro nome do usuário. Se tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 letras "Seu nome é muito grande".
"""
nome = input("Digite o seu nome")
qtd = len(nome)

if qtd <= 4:
    print("Seu nome é curto")
elif qtd <=6:
    print("Seu nome é normal")
else:
    print("Seu nome é longo.")