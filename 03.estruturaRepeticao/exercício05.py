''' Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.'''
# -------------
# author: Paiva
# -------------

retry = 1

while retry == 1:
    country_A = float(input('Informe a população do país A: '))
    rate_A = float(
        input('País A - Informe agora a taxa de crescimento anual: '))
    country_B = float(input('Informe a população do país B: '))
    rate_B = float(
        input('País B - Informe agora a taxa de crescimento anual: '))
    counter = 0

    if country_A < country_B:
        # Caso a população do país A seja menor que o país B, a taxa do país A tem que ser maior que a taxa do país B
        while country_A < country_B and rate_A <= rate_B:
            rate_A = float(
                input('\nInforme uma nova taxa de crescimento anual para o País A: '))

        while country_A <= country_B:
            country_A += country_A * (rate_A/100)
            country_B += country_B * (rate_B/100)
            counter += 1

        print(
            f'\nSerão necessários {counter} anos.\nPopulação do País A: {country_A:0.0f}\nPopulação do País B: {country_B:0.0f}')

    else:
        # Caso a população do país B seja menor que o país A, a taxa do país B tem que ser maior que a taxa do país A
        while country_B < country_A and rate_B <= rate_A:
            rate_B = float(
                input('\nInforme uma nova taxa de crescimento anual para o País B: '))

        while country_B <= country_A:
            country_A += country_A * (rate_A/100)
            country_B += country_B * (rate_B/100)
            counter += 1

        print(
            f'\nSerão necessários {counter} anos.\nPopulação do País B: {country_B:0.0f}\nPopulação do País A: {country_A:0.0f}')

    retry = int(input('\nGostaria de repetir esta operação? [1]Sim |[2]Não'))
    if retry == 1:
        country_A = 0
    else:
        print('\nAté mais!')
        retry = 2
