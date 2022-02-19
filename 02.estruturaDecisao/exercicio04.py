# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# -------------
# author: Paiva
# -------------

letra = input('Digite uma letra: ')

vogal = 'aeiou'

if letra in vogal:
    print('\nA letra é uma vogal!')
else:
    print('\nA letra é uma consoante!')
