#Exercício 033 - Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
num = int(input("Digite um número para calcular a série: "))
answer = 0
for i in range (1, num+1):
    serie = 1 / i
    print("série(1/{}) = {}".format(i, serie))
    answer = answer + serie
print("Resultado da série:", answer)
