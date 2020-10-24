# Reverso do número.
# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
# -------------
# author: Paiva
# -------------
import os


def reverterNumero(numero):
    reversoNumero = list(reversed(str(numero)))
    return reversoNumero


numero = int(input('Informe um número: '))
print(f'O inverso do número {numero} é: {reverterNumero(numero)}.')
