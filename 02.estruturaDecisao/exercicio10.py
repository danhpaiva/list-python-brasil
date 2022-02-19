'''Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
# -------------
# author: Paiva
# -------------

turno = input(
    'Em que turno você estuda: M-matutino | V-vespertino | N-Noturno ').upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')
