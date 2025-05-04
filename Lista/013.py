#Exercício 013 - Receba a quantidade de alimento em quilos. Calcule e mostre a quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
kg = float(input("Digite a quantidade de alimento em quilos (kg): "))
#conversão em mg:
mg = (kg * 1000)
dias = int((mg / 50))
print("quantidade de dias que o alimento de {} kg durará: {} dias".format(kg, dias))
