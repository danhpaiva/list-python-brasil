# Faça um programa que leia 5 números e informe o maior número.
# -------------
# author: Paiva
# -------------
number = [0, 0, 0, 0, 0]

for i in range(5):
    number[i] = float(input('Informe o número: '))

print(max(number))
