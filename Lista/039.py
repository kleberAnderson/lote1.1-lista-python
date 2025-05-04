#Exercício 039 - Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
#Casa: 1 2 3 4 ... 64
#Qtde: 1 2 4 8 ... N
for i in range(64):
    qtde = 2 ** i
    print("Casa ({}) = Qtde ({})".format(i + 1, qtde))
