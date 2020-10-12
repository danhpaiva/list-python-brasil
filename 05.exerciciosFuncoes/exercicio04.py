# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’,
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
# -------------
# author: Paiva
# -------------

def Imprimir(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'


numero = int(input("Informe um número: "))
print(Imprimir(numero))
