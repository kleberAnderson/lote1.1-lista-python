#Exercício 042 - Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99.
d = 1
soma = 0
for i in range(1, 51):
    res = i / d
    soma = soma + res
    print("({}/{}) = {}".format(i, d, res))
    d = d + 2
print("Resultado da soma da série: ({})".format(soma))

