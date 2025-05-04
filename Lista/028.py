#Exercício 028 - Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
#   Venda Mensal         Preço Atual       Preço      Novo
#   < 500                < 30              +          10%
#   >= 500 e < 1000      >= 30 e < 80      +15%
#   >= 1000              >= 80             -          5%
#   obs: para outras condições, preço novo será igual ao preço atual.
preco = float(input("Digite o preço atual do produto: "))
media = float(input("Digite a média de vendas do produto: "))
if preco >= 80:
    if media >= 1000:
        preco = preco * 0.95
        print("Novo preço: {} R$!".format(preco))
    else:
        print("Preço atual: {} R$!".format(preco))
elif preco >= 30:
    if 1000 > media >= 500:
        preco = preco * 1.15
        print("Preço novo: {} R$!".format(preco))
    else:
        print("Preço atual: {} R$!".format(preco))
elif media < 500:
    preco = preco * 1.10
    print("Preço novo: {} R$!".format(preco))
else:
    print("Preço atual: {} R$!".format(preco))