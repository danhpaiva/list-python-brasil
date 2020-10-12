# Faça um programa que leia 5 números e informe a soma e a média dos números.
# -------------
# author: Paiva
# -------------
number = [0, 0, 0, 0, 0]
soma = 0

for i in range(5):
    number[i] = float(input('Informe o número: '))
    soma += number[i]

print(f'Soma: {soma}')
print(f'Média: {soma / 5}')
