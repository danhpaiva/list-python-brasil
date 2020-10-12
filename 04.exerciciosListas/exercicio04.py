# Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.
# -------------
# author: Paiva
# -------------

vetor = []
consoantes = 0

print('Informe os caracteres: ')
for i in range(10):
    vetor.append(input('Caracter: '))
    char = vetor[i]
    if char not in ('a', 'e', 'i', 'o', 'u'):
        consoantes += 1

print(f'Foram lidas: {consoantes} consoantes')
