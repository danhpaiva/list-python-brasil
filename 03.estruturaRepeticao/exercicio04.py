''' Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do 
país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''
# -------------
# author: Paiva
# -------------

country_A = 80000
country_B = 200000
counter = 0

while country_A <= country_B:
    country_A += country_A * (3/100)
    country_B += country_B * (1.5/100)
    counter += 1

print(
    f'\nSerão necessários {counter} anos, onde a população do País A: {country_A:0.0f} ultrapasse a população do País B: {country_B:0.0f}')
