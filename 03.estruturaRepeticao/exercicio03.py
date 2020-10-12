'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd' '''
# -------------
# author: Paiva
# -------------

nome = input("Informe um nome que seja maior que 3 caracteres: ")
while len(nome) <= 3:
    nome = input("Informe um nome que seja maior que 3 caracteres: ")

idade = int(input("Informe uma idade entre 0 e 150 anos "))
while idade < 0 or idade > 150:
    idade = int(input("Informe uma idade entre 0 e 150 anos "))

salario = float(input("Informe um salário maior que zero "))
while salario <= 0:
    salario = float(input("Informe um salário maior que zero "))

sexo = input("Informe o sexo (f/m): ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Informe o sexo (f/m): ")

civil = input("Informe o estado civil (s / c / v / d): ")
while not civil in 'scvd':
    sexo = input("Informe o estado civil (s / c / v / d): ")

print("Cadastro efetuado com sucesso!")
