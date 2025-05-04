#Exercício 027 - Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
numv = int(input("Digite o número de voltas: "))
extm = float(input("Digite a extensão do circuito (em metros): "))
temp = int(input("Digite o tempo de duração (em minutos): "))
km = numv * extm
h = temp * 60
km = km / h
vel = km * 3.6
print("Velocidade média: {} km/h!".format(vel))
