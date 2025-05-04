#Exercício 037 - Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N'nésimo termo.
num = int(input("Digite um número para demonstrar a série Fibonacci até esse valor:"))
f = 0
a = 0
b = 0
print("Série Fibonacci:")
while f <= num:
    print(f)
    if f == 0:
        f = 1
        print(f)
    a = b
    b = f
    f = a + b


