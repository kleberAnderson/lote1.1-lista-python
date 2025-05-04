#Exercício 026 - Receba 2 números inteiros. Verifique e mostre se o maior número é multiplo do menor.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    if num1 % num2 == 0:
        print("{} é multiplo de {}!".format(num1, num2))
    else:
        print("{} não é multiplo de {}!".format(num1, num2))
elif num2 > num1:
    if num2 % num1 == 0:
        print("{} é multiplo de {}!".format(num2, num1))
    else:
        print("{} não é multiplo de {}!".format(num2, num1))
else:
    print("Números iguais! {} e {} ambos multiplos.".format(num1, num2))