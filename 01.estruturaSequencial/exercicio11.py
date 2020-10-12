'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo .
- a soma do triplo do primeiro com o terceiro.
- o terceiro elevado ao cubo.'''
# -------------
# author: Paiva
# ------------- 

numeroInt1 = int(input("Informe o 1º número inteiro: "))
numeroInt2 = int(input("Informe o 2º número inteiro: "))
numeroReal = float(input("Informe um número real: "))

# Cálculo1
operacao1 = (numeroInt1 * 2) * (numeroInt2 / 2)

# Cálculo2
operacao2 = (3 * numeroInt1) + numeroReal

# Cálculo3
operacao3 = (numeroReal ** 3)

print("O produto do dobro do primeiro com metade do segundo: " + str(operacao1))
print("A soma do triplo do primeiro com o terceiro: " + str(operacao2))
print("O terceiro elevado ao cubo: " + str(operacao3))
