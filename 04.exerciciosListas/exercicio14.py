'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''
# -------------
# author: Paiva
# -------------
import os
os.system('cls')

list_questions = []
counter = 0

list_questions.append(int(input('Telefonou para a vítima? [1]Sim [2]Não: ')))
list_questions.append(int(input('Esteve no local do crime? [1]Sim [2]Não: ')))
list_questions.append(int(input('Mora perto da vítima? [1]Sim [2]Não: ')))
list_questions.append(int(input('Devia para a vítima? [1]Sim [2]Não: ')))
list_questions.append(int(input('Telefonou para a vítima: [1]Sim [2]Não: ')))

for i in range(5):
    if list_questions[i] == 1:
        counter += 1

os.system('cls')
if counter == 2:
    print(f'Classificação: Suspeita')
elif counter == 3 or counter == 4:
    print(f'Classificação: Cúmplice')
elif counter == 5:
    print(f'Classificação: Assassino')
else:
    print(f'Classificação: Inocente')
