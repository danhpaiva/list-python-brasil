# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# -------------
# author: Paiva
# -------------
import os
import random

lista_um = []
lista_dois = []
lista_tres = []
numero_lista_dois = 0

for i in range(10):
    lista_um.append(random.randrange(10, 50))
    lista_dois.append(random.randrange(10, 50))

for i in range(10):
    lista_tres.append(lista_um[i])
    for j in range(1):
        lista_tres.append(lista_dois[numero_lista_dois])
        numero_lista_dois += 1

    
os.system('cls')
print(f'Lista 01:\n {lista_um}')
print(f'Lista 02:\n {lista_dois}')
print(f'Lista 03(valores intercalados):\n {lista_tres}')
