'''
Nome ao contrário em maiúsculas. 
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. 
'''
# -------------
# author: Paiva
# -------------
def informarNome():
    nome = input("Informe seu primeiro nome: ").upper()
    return nome

def inverterNome():
    nome = informarNome()
    print(nome[::-1])

inverterNome()