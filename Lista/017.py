#Exercício 017 - Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/L.
#Receber o tempo de percurso e a velocidade média.
tempcurso = float(input("Digite o tempo do percurso em Horas: "))
velmedia = int(input("Digite a velocidade média em Km/h: "))
percurso = (tempcurso * velmedia)
litros = (percurso / 12)
print("Quantidade de litros gastos em na viagem: {} L".format(litros))
