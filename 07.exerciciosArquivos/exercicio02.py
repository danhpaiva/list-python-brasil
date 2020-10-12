'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, 
ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. 
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, 
que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal. 
'''
# -------------
# author: Paiva
# -------------

with open('usuarios.txt') as arquivo:
    listaUsuarios = arquivo.read().splitlines()
    arquivo.close()


def main():
    arquivoEscrita = open("relatório.txt", "w")

    arquivoEscrita.write(
        "ACME Inc.               Uso do espaço em disco pelos usuários\n------------------------------------------------------------------------\n")
    arquivoEscrita.write("Nr.\tUsuário\t\tEspaço utilizado\t\t% do uso\n")

    contador = 1  # Pegar índice de usuários
    global totalEspaco
    totalEspaco = 0

    for linha in listaUsuarios:  # For para pegar o total de espaço utilizado do HD
        valor = linha.split()
        totalEspaco += int(valor[1])

    totalEspaco = conversaoDados(totalEspaco)

    for dado in listaUsuarios:  # for para manipular a impressão dos dados dos usuários
        valor = dado.split()
        arquivoEscrita.write(str(contador) + "\t" + str(valor[0]) + "\t\t" + str(
            conversaoDados(valor[1])) + "\t\t\t" + str(calculoPercentual(valor[1], totalEspaco)) + "\n")
        contador += 1

    arquivoEscrita.write("\nEspaço total ocupado:" + str(totalEspaco) + "\n")
    arquivoEscrita.write("Espaço médio ocupado:" +
                         str(calcularMedia((contador - 1), totalEspaco)))
    arquivoEscrita.close()


def conversaoDados(valor1):
    espaco = float(valor1)
    espaco /= 1048576  # 1024 x 1024
    espaco = round(espaco, 2)  # Função para pegar duas casas decimais
    return espaco


def calculoPercentual(valor1, totalEspaco):
    # Chamando a conversão para pegar o valor correto para a porcentagem
    porcentagem = conversaoDados(valor1)
    porcentagem /= totalEspaco
    porcentagem *= 100
    porcentagem = round(porcentagem, 2)
    return porcentagem


def calcularMedia(contador, totalEspaco):
    media = totalEspaco / contador
    media = round(media, 2)
    return media


main()  # Ínicio Programa
