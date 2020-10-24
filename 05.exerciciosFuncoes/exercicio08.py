# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
# -------------
# author: Paiva
# -------------
import os


def contarDigitos(numero):
    tamanho = len(str(numero))
    return tamanho


numero = int(input('Informe um número: '))
print(
    f'A quantidade de dígitos do número {numero} é: {contarDigitos(numero)}.')
