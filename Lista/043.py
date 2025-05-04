#Exercício 043 - Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1.10m
# e cresce 3 cm ao ano e Maria tem 1.5 m e cresce 2 cm ao ano.

ana = 1.1
maria = 1.5
ano = 0
while maria >= ana:
    ana = ana + 0.03
    maria = maria + 0.02
    ano = ano + 1
print("São necessários {} anos para que Ana seja maior que Maria.\n Ana: {} m\n Maria: {} m".format(ano, ana, maria))
