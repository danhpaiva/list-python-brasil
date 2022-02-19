''' Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''
# -------------
# author: Paiva
# -------------

base = int(input('Informe a base: '))
exponent = int(input('Informe o expoente: '))
result = 1
counter = 1

while counter <= exponent:
    result *= base
    counter += 1

print(f'\nResultado de {base} elevado a {exponent}: {result}')
