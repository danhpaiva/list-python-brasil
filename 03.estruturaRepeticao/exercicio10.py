'''Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.'''
# -------------
# author: Paiva
# -------------

number_one = int(input('Informe o primeiro número inteiro: '))
number_two = int(input('Informe o segundo número inteiro: '))

if number_one > number_two:
    for numbers in range(number_two, number_one, 1):
        print(numbers)
elif number_two > number_one:
    for numbers in range(number_one, number_two, 1):
        print(numbers)
else:
    print('Números iguais!')