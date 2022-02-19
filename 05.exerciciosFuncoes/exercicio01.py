# Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário.
# Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
# -------------
# author: Paiva
# -------------

def ImprimirSequencia(n):
    for c in range(1, n + 1):
        cont = 1
        while True:
            print(c, end=' ')
            if cont == c:
                break
            cont += 1
        print()


n = int(input('Informe um número(limite): '))
ImprimirSequencia(n)
