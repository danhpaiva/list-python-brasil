# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# -------------
# author: Paiva
# -------------
import os
import random

lista_um = []
lista_dois = []
lista_tres = []
lista_quatro = []
numero_lista_dois = 0
numero_lista_tres = 0

for i in range(10):
    lista_um.append(random.randrange(10, 90))
    lista_dois.append(random.randrange(10, 90))
    lista_tres.append(random.randrange(10, 90))

for i in range(10):
    lista_quatro.append(lista_um[i])
    for j in range(1):
        lista_quatro.append(lista_dois[numero_lista_dois])
        numero_lista_dois += 1
        for k in range(1):
            lista_quatro.append(lista_tres[numero_lista_tres])
            numero_lista_tres += 1


os.system('cls')
print(f'Lista 01:\n {lista_um}')
print(f'Lista 02:\n {lista_dois}')
print(f'Lista 03:\n {lista_tres}')
print(f'Lista 04(valores intercalados):\n {lista_quatro}')
