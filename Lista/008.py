#Exercício 008 - Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a.m.
ValorP = float(input("Digite o valor do depósito: "))
print("Valor depositado: ",ValorP)
Rend = (ValorP * 0.013)
ValorP = ValorP + Rend
print("Valor corrigido após 1 mês, com rendimento de 1,3% a.m. (R$",ValorP,")")
print("Rendimento de", Rend)
