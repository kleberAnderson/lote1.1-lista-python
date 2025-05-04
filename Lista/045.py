#Exercício 045 - Calcule e mostre a série 1 - 2/4 + 3/9 - 4/16 + 5/25 + ... + 15/225.
soma = 0
for i in range(1, 16):
    d = i ** 2
    div = i / d
    if i % 2 == 0:
        div = -1 * div
        print("-{}/{} = {}".format(i, d, div))
        soma = soma + div
    print("+{}/{} = {}".format(i, d, div))
    soma = soma + div
print("Resultado da soma da série: ({})".format(soma))

