# Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.
# -------------
# author: Paiva
# -------------
vetor_A = []
numero = 1
soma = 0

for i in range(10):
    vetor_A.append(int(input(f'Digite o {numero}º número: ')))
    vetor_A[i] = vetor_A[i] ** 2
    soma += vetor_A[i]
    numero += 1

print(f'A soma dos quadrados dos elementos é {soma}')
