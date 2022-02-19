# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.
# -------------
# author: Paiva
# -------------
import os
import random

os.system('cls')

lista_altura = [
    1.33, 1.41, 1.65, 1.68, 1.82,
    1.12, 1.56, 1.65, 1.68, 1.84,
    1.64, 1.44, 1.65, 1.68, 1.86,
    1.31, 1.42, 1.65, 1.68, 1.88,
    1.32, 1.47, 1.65, 1.68, 1.81,
    1.33, 1.49, 1.65, 1.68, 1.83
]
lista_idade = []
media_altura = 0
contador = 0

for i in range(30):
    media_altura += lista_altura[i]
    lista_idade.append(random.randint(6, 18))

media_altura = media_altura / 30

for i in range(30):
    if lista_idade[i] > 13:
        if lista_altura[i] < media_altura:
            contador += 1

print(f'Lista alturas:\n{lista_altura}')
print(f'Lista idades:\n{lista_idade}')

print(f'Existem {contador} alunos com idade > 13 e altura < media.')
