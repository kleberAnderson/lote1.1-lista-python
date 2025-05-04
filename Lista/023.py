#Exercício 023 - Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
#Mostre os 4 números em ordem crescente:
print("Digite três valor em ordem crescente:")
n1 = float(input("Digite o 1º valor: "))
n2 = float(input("Digite o 2º valor: "))
n3 = float(input("Digite o 3º valor: "))
print("Digite 0 4º valor em fora de ordem:")
n = float(input("Digite o 4º valor: "))
if n > n3:
    print(n1,  n2,  n3,  n)
elif n > n2:
    print(n1,  n2,  n,  n3)
elif n > n1:
    print(n1,  n,  n2,  n3)
else:
    print(n,  n1,  n2,  n3)

