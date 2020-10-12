# Faça um Programa que leia três números e mostre o maior deles.
# -------------
# author: Paiva
# -------------

numeroUm = float(input('Digite o primeiro número: '))
numeroDois = float(input('Digite o segundo número: '))
numeroTres = float(input('Digite o terceiro número: '))

if numeroUm > numeroDois and numeroUm > numeroTres:
    print("O maior número é o : " + str(numeroUm))
elif numeroDois > numeroUm and numeroDois > numeroTres:
    print("O maior número é o : " + str(numeroDois))
else:
    print("O maior número é o : " + str(numeroTres))
