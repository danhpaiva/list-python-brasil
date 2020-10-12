'''Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
# -------------
# author: Paiva
# -------------

number = int(input('Informe um número de 1 a 7: '))

if number == 1:
    print('Domingo')
elif number == 2:
    print('Segunda')
elif number == 3:
    print('Terça')
elif number == 4:
    print('Quarta')
elif number == 5:
    print('Quinta')
elif number == 6:
    print('Sexta')
elif number == 7:
    print('Sábado')
else:
    print('Valor Inválido')
