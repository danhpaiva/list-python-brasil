# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
# -------------
# author: Paiva
# -------------
import os
os.system('cls')

lista_temperatura = []
mes = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

media_anual = 0

for i in range(12):
    lista_temperatura.append(
        float(input(f'Informe a temperatura do mês de {mes[i]}:')))
    media_anual += lista_temperatura[i]

media_anual = media_anual / 12

os.system('cls')
print(f'Média Anual: {media_anual}')
for i in range(12):
    if lista_temperatura[i] > media_anual:
        print(f'Temperatura: {lista_temperatura[i]}\nMês: {i} - {mes[i]}')
