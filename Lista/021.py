#Exercício 021 - Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média.
n1 = float(input("Digite a 1º nota bimestral: "))
n2 = float(input("Digite a 2º nota bimestral: "))
n3 = float(input("Digite a 3º nota bimestral: "))
n4 = float(input("Digite a 4º nota bimestral: "))
media = (n1+n2+n3+n4)/4
print("Média bimestral: {}".format(media))
if media >= 6:
    print("APROVADO.")
elif 6 > media >= 3:
    print("EXAME.")
elif media < 3:
    print("RETIDO.")