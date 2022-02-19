# Faça um Programa que leia três números e mostre o maior e o menor deles
# -------------
# author: Paiva
# -------------
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 < n3:
    n1, n3 = n3, n1

if n1 < n2:
    n1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2
print('A ordem decrescente é: ', n1, n2, n3)
