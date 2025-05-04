#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes.
#Calcule  salário que serão as horas trabalhadas X o valor por hora. Calcule o salário líquido ( = Saário Bruto - desconto).
#A cada dependente será acrescido R$ 100,00 no Salário Líquido. Exiba o salário a receber.
qtdhoras = int(input("Digite a quantidade de horas trabalhadas: "))
valorphora = float(input("Digite o valor por hora: "))
percentd = float(input("Digite o percentual de desconto: "))
numdep = int(input("Digite o nº de dependente: "))
#Caculo do salário Bruto:
salb = (qtdhoras * valorphora)
#Calculo do percentual de desconto:
desc = salb * percentd
#Calculo do salário líquido e nº de descendente:
sall = (salb - desc)
sall = (sall + (numdep * 100))
#mensagem:
print("Salário a receber: R$ {}".format(sall))
