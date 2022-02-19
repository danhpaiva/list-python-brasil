# Faça um Programa que peça dois números e imprima o maior deles.
# -------------
# author: Paiva
# -------------

numeroUm = int(input("Informe o primeiro número: "))
numeroDois = int(input("Informe o segundo número: "))

if numeroUm > numeroDois:
    print("O número " + str(numeroUm) + " é o maior.")
elif numeroDois > numeroUm:
    print("O número " + str(numeroDois) + " é o maior.")
else:
    print("Os números são iguais.")
