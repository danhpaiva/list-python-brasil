# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
# -------------
# author: Paiva
# -------------

print("\tCálculo do Peso Ideal\n")

altura = float(input("Informe a sua altura: "))

pesoIdeal = (72.7 * altura) - 58
pesoIdeal = round(pesoIdeal, 2)

print("Seu peso ideal é de: " + str(pesoIdeal) + " Kg.")
