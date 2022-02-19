'''Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F
'''
# -------------
# author: Paiva
# -------------


def informarNome():
    nome = input("Informe seu nome: ")
    return nome


def imprimirNomeVertical():
    nome = informarNome()
    print()
    
    tamanho = len(nome)
    contador = 0
    nomeReduzido = " ".join(nome)
    nomeReduzido = nomeReduzido.split(" ")

    while tamanho > contador:
        if contador == 0:
            print(nome)
        else:
            nomeReduzido.pop()
            print("".join(nomeReduzido))
        contador += 1

imprimirNomeVertical()
