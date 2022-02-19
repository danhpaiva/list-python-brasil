'''Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
import os
os.system('cls')
print('Gerenciador de Download')

size = float(input('Informe o tamanho do arquivo do download(MB): '))

velocity = float(input('Informe a velocidade do link de Internet: '))

time = size / velocity
time_minute = time / 60

print(
    f'O tempo para download deste arquivo é de: {round(time_minute, 2)} minutos.')
