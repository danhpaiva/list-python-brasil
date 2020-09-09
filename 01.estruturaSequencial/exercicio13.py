'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
'''


def main():
    print("\tCálculo do Peso Ideal\n")
    sexo = input("Informe seu sexo: [F]Feminino | [M]Masculino: ").upper()
    h = float(input("Informe a sua altura: "))
    print("Seu peso ideal é de: " + str(CalcularPeso(sexo, h)) + " Kg.")


def CalcularPeso(sexo, h):
    global pesoIdeal
    if sexo == "M":
        pesoIdeal = (72.7 * h) - 58
        pesoIdeal = round(pesoIdeal, 2)
        return pesoIdeal
    elif sexo == "F":
        pesoIdeal = (62.1 * h) - 44.7
        pesoIdeal = round(pesoIdeal, 2)
        return pesoIdeal
    else:
        return "Sexo inválido!"


main()
