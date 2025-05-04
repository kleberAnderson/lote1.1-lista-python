#Exercício 032 - Receba um número inteiro. Calcule e mostre seu fatorial.
num = int(input("Digite um número para calcular seu fatorial.\n : "))
r = 1
for i in range (num, 1, -1):
    r = r * i
print(r)

