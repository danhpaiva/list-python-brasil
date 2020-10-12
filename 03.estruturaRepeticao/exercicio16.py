'''A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.'''
# -------------
# author: Paiva
# -------------

last_number = 0
penultimate_number = 1
term = 0

print('\tSérie de Fibonacci')
count = 1

print(last_number)
while term <= 500:
    term = last_number + penultimate_number
    penultimate_number = last_number
    last_number = term
    count += 1
    print(term)
