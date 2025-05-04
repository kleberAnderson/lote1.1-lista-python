#Exercício 034 - Receba um número. Calcule e mostre os resultados da tabuada desse número.
num = int(input("Digite um número para mostrar os resultados da tabuada: "))
for i in range(11):
    ans = num * i
    print("{} * {} = ({})".format(i, num, ans))
