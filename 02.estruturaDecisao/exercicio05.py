''' Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
# -------------
# author: Paiva
# -------------

notaUm = float(input('Informe a primeira nota: '))
notaDois = float(input('Informe a segunda nota: '))

mediaNota = (notaUm + notaDois) / 2

print(mediaNota)

if mediaNota >= 7:
    if mediaNota == 10:
        print('Aprovado com Distinção!')
    else:
        print('Aprovado')
else:
    print('Reprovado')
