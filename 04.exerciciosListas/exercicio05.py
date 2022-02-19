# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.
# -------------
# author: Paiva
# -------------
import os

vetorInteiro = []
vetorImpar = []
vetorPar = []
contador = 1

for i in range(20):
    vetorInteiro.append(int(input(f'Informe o {contador}º número: ')))
    contador += 1

for i in range(20):
    if vetorInteiro[i] % 2 == 0:
        vetorPar.append(vetorInteiro[i])
    else:
        vetorImpar.append(vetorInteiro[i])

os.system('cls')
print(f'Vetor Inteiro: {vetorInteiro}')
print(f'Vetor Ímpar: {vetorImpar}')
print(f'Vetor Par: {vetorPar}')
