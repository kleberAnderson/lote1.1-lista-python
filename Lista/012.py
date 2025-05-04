#Exercício 012 - Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
Nasc = int(input("Digite o ano de nascimento: "))
Atual = int(input("Digite o ano atual: "))
IdadeP = (Atual - Nasc)
IdadeF = (IdadeP + 17)
print("Idade atual {}".format(IdadeP))
print("Idade daqui a 17 anos no futuro: {}".format(IdadeF))
