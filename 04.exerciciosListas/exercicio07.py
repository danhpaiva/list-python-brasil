# Faça um Programa que leia um vetor de 5 números inteiros,
# mostre a soma, a multiplicação e os números.
# -------------
# author: Paiva
# -------------
import os

lista_numero = []
soma = 0
multiplicacao = 1
numero = 1

for i in range(5):
    lista_numero.append(int(input(f'Informe o {numero}º número: ')))
    soma += lista_numero[i]
    multiplicacao *= lista_numero[i]
    numero += 1

os.system('cls')
print(f'Números Informados: {lista_numero}')
print(f'\nSoma: {soma}')
print(f'\nMultiplicação: {multiplicacao}')
