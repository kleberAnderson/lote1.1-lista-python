#Exercício 032 - Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
from distutils.command.install_egg_info import safe_version

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
while num1 > num2:
    save = num1
    num1 = num2
    num2 = save
print("Maior número ({}).".format(num2))
answer = 0
if num1 % 2 == 0:
    for i in range(num1 + 1, num2 + 1, 2):
        answer = answer + i
    print("Somatória dos número ímpares: {}".format(answer))
else:
    for i in range(num1, num2 + 1, 2):
        answer = answer + i
    print("Somatória dos números ímpares: {}".format(answer))