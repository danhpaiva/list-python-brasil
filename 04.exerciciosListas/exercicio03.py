# Faça um Programa que leia 4 notas, mostre as notas e a média na tela
# -------------
# author: Paiva
# -------------

lista_nota = []
contador = 1
media = 0

for i in range(4):
    lista_nota.append(float(input(f'Informe a {contador}ª nota: ')))
    media += lista_nota[i]
    contador += 1

print()
contador = 1
for i in range(4):
    print(f'Nota {contador}: {lista_nota[i]}')
    contador += 1

media = media / 4
print(f'Média: {media}')
