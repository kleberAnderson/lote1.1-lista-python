#Exercício 022 - Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 == num2:
    print("Números iguais.")
elif num1 > num2:
    print("Números em ordem crescente:")
    print(num2, num1)
else:
    print("Números em ordem crescente:")
    print(num1, num2)