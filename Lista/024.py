#Exercício 024 - Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3:
num = int(input("Digite um valor inteiro: "))
if num % 2 == 0 and num % 3 == 0:
    print("{} é divisível por 2 e 3.".format(num))
elif num % 2 == 0:
    print("{} é divisível por 2.".format(num))
elif num % 3 == 0:
    print("{} é divisível por 3.".format(num))
else:
    print("{} não é divisível por 2 e 3".format(num))