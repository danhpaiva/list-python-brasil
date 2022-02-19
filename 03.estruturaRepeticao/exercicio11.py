# Altere o programa anterior para mostrar no final a soma dos números.
# -------------
# author: Paiva
# -------------

number_one = int(input('Informe o primeiro número inteiro: '))
number_two = int(input('Informe o segundo número inteiro: '))
soma = 0

if number_one > number_two:
    for numbers in range(number_two, number_one, 1):
        soma += numbers
        print(numbers)
    print(f'A soma dos números é {soma}.')
elif number_two > number_one:
    for numbers in range(number_one, number_two, 1):
        soma += numbers
        print(numbers)
    print(f'A soma dos números é {soma}.')
else:
    print('Números iguais!')
