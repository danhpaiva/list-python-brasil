'''Faça um programa que peça 10 números inteiros, calcule e mostre a 
quantidade de números pares e a quantidade de números impares.'''
# -------------
# author: Paiva
# -------------

numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counter = 1
counter_odd = 0
counter_pair = 0

for number in range(10):
    numbers[number] = int(input(f'Informe o {counter}º número: '))
    counter += 1

for number in range(10):
    if numbers[number] % 2 == 0:
        counter_pair += 1
    else:
        counter_odd += 1

print(f'\nExistem {counter_odd} números ímpares e {counter_pair} números pares.')
