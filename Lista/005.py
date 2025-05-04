#Exercício 005 - Receba os coeficientes A, B e Cde uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue 2 raízes).
from math import sqrt
A = int(input("Digite o coeficiente A: "))
B = int(input("Digite o coeficiente B: "))
C = int(input("Digite o coeficiente C: "))
Delta = int((B**2) -4*A*C)
Delta = sqrt(Delta)
X1 = (-B + Delta)/(2*A)
X2 = (-B - Delta)/(2*A)
print("Raízes reais: X1 =", X1, ",  X2 =",X2)

