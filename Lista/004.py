#Exercício 004 - Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em Fahrenheit.
Cel = int(input("Digite a temperatura atual em graus Celsius: "))
F = float((9 * Cel + 160)/5)
print("A temperatura atual: graus Celsius(",Cel,"ºC) - Fahrenheit(",F,"ºF)")