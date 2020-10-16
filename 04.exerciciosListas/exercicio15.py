'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;'''
import os
os.system('cls')

list_note = []
check = 1
counter = 0

while check != -1:
    os.system('cls')
    list_note.append(float(input('Informe uma nota: ')))
    if list_note[-1] == -1:
        check = -1
    else:
        counter += 1

print(f'Foram lidos {counter} valores.')
