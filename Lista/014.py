#Exercício 014 - Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.
print("Digite as informações de um triângulo em Graus")
ang1 = int(input("Digite o 1º ângulo: "))
ang2 = int(input("Digite 0 2º ângulo: "))
ang3 = (180 - (ang1 + ang2))
print("Valores dos ângulos do triângulo em Graus: 1ª ângulo: {}º, 2º ângulo: {}º, 3º ângulo: {}º".format(ang1, ang2, ang3))