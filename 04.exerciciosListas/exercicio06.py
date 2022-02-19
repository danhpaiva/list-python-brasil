# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
# -------------
# author: Paiva
# -------------
import os

lista_nota = []
media = []
aluno = 1
contador_aluno_aprovado = 0

print('\nNotas dos Alunos')
for i in range(10):
    print()
    soma = 0
    for j in range(4):
        nota = int(input(f'Notas do {aluno}º aluno: '))
        lista_nota.append(nota)
        soma += nota
    aluno += 1
    media.append(soma/4)

for i in range(10):
    if media[i] >= 7:
        contador_aluno_aprovado += 1

os.system('cls')
print(f'Médias: {media}\n')
print(f'Existem: {contador_aluno_aprovado} alunos aprovados')
