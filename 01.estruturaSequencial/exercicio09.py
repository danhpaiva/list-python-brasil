# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# -------------
# author: Paiva
# -------------

f = input("Informe a temperatura em Fahrenheit: ")

c = 5 * ((float(f) - 32) / 9)

print("A temperatura é de " + str(c) + " graus Celsius")
