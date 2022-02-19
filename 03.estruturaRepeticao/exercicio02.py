''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''
# -------------
# author: Paiva
# -------------

print('\nCadastro de Usuário')
name_user = input('Informe o seu nome de usuário: ')
password = input('Informe sua senha: ')

while name_user == password:
    print('\n\tERRO: Nome de usuário e senha não podem ser iguais.')
    name_user = input('Informe o seu nome de usuário: ')
    password = input('Informe sua senha: ')
else:
    print('\nCadastro realizado com sucesso!')
