#Exercício 044 - Receba o número da base e do expoente. Calcule e mostre o valor da potência.
base = int(input("Digite o número da base: "))
exp = int(input("Digite o número do expoente: "))
res = 1
for i in range(1, exp+1):
    res = res * base
print("{} ** {} = {}".format(base, exp, res))