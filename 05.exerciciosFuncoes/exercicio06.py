# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
# -------------
# author: Paiva
# -------------
import os


def converter_hour(hour, minute):
    if hour > 12 and hour != 24:
        counter = 0
        for i in range(hour):
            if i >= 12:
                counter += 1
        return counter
    elif hour == 24:
        return 0
    else:
        return hour


def print_message(hour, minute):
    print(f'Conversão: {converter_hour(hour, minute)}:{minute}.')


retry = 1
while retry == 1:
    os.system('cls')
    print('\tConversor de Horas\n')
    hour = int(input('Digite a hora para a conversão: '))
    minute = int(input('Digite os minutos: '))
    A = 'A.M'
    P = 'P.M'
    print_message(hour, minute)
    retry = int(input('Realizar mais uma conversão: [1]Sim | [2]Não'))
print('Até mais!')
