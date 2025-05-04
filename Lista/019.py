#Exercício 019 - Receba 2 valores reais. Calcule e mostre o maior deles.
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
print("num1: {}, num2: {}".format(num1, num2))
if num1 > num2:
    print("O maior número é {}".format(num1))
elif num2 > num1:
    print("O maior número é {}".format(num2))
else:
    print("Números iguais!")