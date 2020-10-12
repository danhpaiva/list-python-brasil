''' Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

O algoritmo deve mostrar na tela:
as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.'''
# -------------
# author: Paiva
# -------------

nota_parcial_um = float(input('Informe a primeira nota: '))
nota_parcial_dois = float(input('Informe a segunda nota: '))

media = (nota_parcial_um + nota_parcial_dois) / 2

print('\nNota Parcial 01: ' + str(nota_parcial_um))
print('Nota Parcial 02: ' + str(nota_parcial_dois))
print('Média: ' + str(media))

if media >= 9 and media <= 10:
    print('Conceito: A\nAprovado')
elif media >= 7.5 and media < 9:
    print('Conceito: B\nAprovado')
elif media >= 6 and media < 7.5:
    print('Conceito: C\nAprovado')
elif media >= 4 and media < 6:
    print('Conceito: D\nReprovado')
else:
    print('Conceito: E\nReprovado')
