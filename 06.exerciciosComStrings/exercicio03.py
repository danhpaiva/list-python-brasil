'''Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
F
U
L
A
N
O
'''
# -------------
# author: Paiva
# -------------

def informarNome():
    nome = input("Informe seu nome: ")
    return nome


def imprimirNomeVertical():
    nome = informarNome()
    print("\n".join(nome))


imprimirNomeVertical()
