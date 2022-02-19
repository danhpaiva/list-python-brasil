'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos.

    O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

    O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''
# -------------
# author: Paiva
# -------------
arquivoLeitura = open("IP.txt", "r")
arquivoEscrita = open("ip_saida.txt", "w")

arquivoEscrita.write("[Endereços válidos:]\n")
for linha in arquivoLeitura:
    valores = linha.split()
    if valores == ['200.135.80.9'] or valores == ['192.168.1.1'] or valores == ['8.35.67.74'] or valores == ['1.2.3.4']:
        arquivoEscrita.write(str(valores) + "\n")

arquivoLeitura.close()
arquivoEscrita.close()


arquivoLeitura = open("IP.txt", "r")
arquivoEscrita = open("ip_saida.txt", "a")
arquivoEscrita.write("[Endereços inválidos:]\n")
for linha in arquivoLeitura:
    valores = linha.split()
    if valores == ['257.32.4.5'] or valores == ['85.345.1.2'] or valores == ['9.8.234.5'] or valores == ['192.168.0.256']:
        arquivoEscrita.write(str(valores) + "\n")

arquivoLeitura.close()
arquivoEscrita.close()
