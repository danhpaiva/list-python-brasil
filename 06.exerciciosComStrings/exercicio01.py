'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

    Compara duas strings
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
'''
# -------------
# author: Paiva
# -------------


def informarString():
    string = input("Informe a string: ")
    return string


def imprimirString(string, numero):
    print("String", numero, " :", string)


def verificarTamanhoString(string):
    print("Tamanho de ", string, " :", len(string), " caracteres.")


string1 = informarString()
string2 = informarString()

print("Compara Duas Strings")
imprimirString(string1, 1)
imprimirString(string2, 2)

print("Verificar Tamanho das Strings")
verificarTamanhoString(string1)
verificarTamanhoString(string2)

if len(string1) == len(string2):
    print("As strings possuem o mesmo tamanho!")
else:
    print("As strings são de tamanhos diferentes!")

if string1 == string2:
    print("As strings possuem o mesmo conteúdo")
else:
    print("As strings possuem conteúdos diferentes!")
