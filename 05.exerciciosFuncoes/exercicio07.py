''' Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso 
e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e 
devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e 
assim continuar até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, 
exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''
# -------------
# author: Paiva
# -------------
import os


def valorPagamento(diasAtraso, valorPrestacao):
    if diasAtraso == 0:
        return valorPrestacao
    else:
        multa = 0
        ''' Multa a ser paga '''
        multa += valorPrestacao * (3 / 100)
        ''' Juros por dia '''
        juros = 0
        juros += (valorPrestacao * (1 / 100)) * diasAtraso
        valorPrestacao += (multa + juros)
        return valorPrestacao


quantPrestacao = 0
repetir = 1
valorTotal = 0

os.system('cls')
print('\tCálculo de Prestações')

while repetir != 0:
    quantPrestacao += 1
    valorPrestacao = float(
        input(f'Informe o valor da prestação nº {quantPrestacao}:'))
    repetir = valorPrestacao
    if repetir == 0:
        diasAtraso = 0
        quantPrestacao += -1
        os.system('cls')
        break
    diasAtraso = int(input('Informe quantos dias estão em atraso: '))
    print(
        f'\nValor a ser pago na prestação nº{quantPrestacao}: {valorPagamento(diasAtraso, valorPrestacao)}')
    valorTotal += valorPagamento(diasAtraso, valorPrestacao)
    input('\nPressione ENTER para continuar')
    os.system('cls')

print(
    f'Relatório Diário:\nQuantidade de Prestações Pagas: {quantPrestacao}\nValor Total de prestações pagas: {valorTotal}')
