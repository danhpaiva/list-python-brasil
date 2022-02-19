# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa
# -------------
# author: Paiva
# -------------

list_number = []

for number in range(10):
    list_number.append(float(input('Informe os números reais: ')))

list_number.reverse()

print(list_number)
