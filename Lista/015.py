#Exercício 015 - Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
from math import sqrt
print("Digite os valores do cateto de um triângulo retãngulo para saber o valor da hipotenusa.")
cat1 = int(input("Digite o valor do primeiro cateto: "))
cat2 = int(input("Digite o valor do segundo cateto: "))
hip = sqrt((cat1 ** 2) + (cat2 ** 2))
print("O valor da Hipotenusa do triângulo retângulo corresponde: {}.".format(hip))
