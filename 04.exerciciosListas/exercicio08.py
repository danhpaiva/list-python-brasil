# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
# -------------
# author: Paiva
# -------------
import os

lista_altura = []
lista_idade = []
pessoa = 1

for i in range(5):
    print(f'\nPessoa nº{pessoa}')
    lista_altura.append(float(input('Informe sua altura: ')))
    lista_idade.append(int(input('Informe sua idade: ')))
    pessoa += 1

lista_altura.reverse()
lista_idade.reverse()

os.system('cls')
print(f'Lista Altura Invertida: {lista_altura}')
print(f'Lista Idade Invertida: {lista_idade}')
