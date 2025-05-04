#Exercício 038 - Receba 100 números inteiros, Verifique e mostre o maior e o menor valor. Obs: somente valores positivos.
i = 1
ma = 0
me = 0
while i <= 5:
    num = int(input("Digite um número inteiros: "))
    if num <= 0:
        print("Número inválido! Digite números positivos.")
    else:
        if i == 1:
            ma = num
            me = num
        elif num > ma:
            ma = num
        elif num < me:
            me = num
        i = i + 1
print("Maior número ({})  -  Menor número ({})".format(ma, me))



