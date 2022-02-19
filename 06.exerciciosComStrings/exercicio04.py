'''Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
F
FU
FUL
FULA
FULAN
FULANO
'''
# -------------
# author: Paiva
# -------------


def informarNome():
    nome = input("Informe seu nome: ")
    return nome


def imprimirNomeVertical():
    nome = informarNome()
    tamanho = len(nome)
    contador = 0
    nomeCompleto = ""
    while contador < tamanho:
        if contador == 0:
            print(nome[contador])
            nomeCompleto += nome[contador]
            contador += 1
        else:
            nomeCompleto += nome[contador]
            print(nomeCompleto)
            contador += 1


imprimirNomeVertical()
