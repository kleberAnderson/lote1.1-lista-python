#Exercício 019 - Receba 2 valores reais. Calcule e mostre o maior deles.
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
#uso da função abs:
valor = abs(v1 - v2)
print("A diferença entre os dois valores reais: {}".format(valor))
