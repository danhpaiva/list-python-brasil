'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''

nome = input("Informe um nome que seja maior que 3 caracteres: ")
while nome <= 3:
    nome = input("Informe um nome que seja maior que 3 caracteres: ")