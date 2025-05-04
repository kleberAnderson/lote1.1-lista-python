#Exercício 036 - Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... +1/N!
num = int(input("Digite um número para calcular a série: "))
soma = 0
for i in range(1, num + 1):
    dnor = 1
    for j in range(1, i + 1):
        dnor = j * dnor
    answer = 1 / dnor
    print("{} / {}! = {}".format(1, i, answer))
    soma = soma + answer
print("Resultado da soma da série:", soma)
