# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# -------------
# author: Paiva
# -------------

n = int(input('Informe um número: '))
last_number = 1
penultimate_number = 1

print('\tSérie de Fibonacci')
if n == 1:
    print('1')
elif n == 2:
    print('1\n1')
else:
    count = 3
    print('1')
    print('1')
    while count <= n:
        term = last_number + penultimate_number
        penultimate_number = last_number
        last_number = term
        count += 1
        print(term)

