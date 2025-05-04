#Exercício 007 - Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
print("Digite as informações do paralelepípedo")
Comp = float(input("Digite o comprimento: "))
Lar = float(input("Digite a largura: "))
Alt = float(input("Digite a altura: "))
Vol = (Comp * Lar * Alt)
print("O volume do paralelepípedo:", Vol)
print(type(Vol))
