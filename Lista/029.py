#Exercício 029 - Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
#Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
tipo = int(input("Digite o tipo de inestimento:\n 1 - Poupança\n 2 - Renda Fixa\n:"))
if tipo == 1:
    i = float(input("Digite o valor do investimento: "))
    r = (i * (1+0.03)**30)
    print("Valor corrigido em 30 dias: {} R$!".format(r))
elif tipo == 2:
    i = float(input("Digite o valor do investimento: "))
    r = (i * (1 + 0.05)**30)
    print("Valor corrigido em 30 dias: {} R$!".format(r))
else:
    print("Inválido!")