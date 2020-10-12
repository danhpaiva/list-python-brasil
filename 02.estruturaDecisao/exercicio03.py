# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# -------------
# author: Paiva
# -------------

letra = input('Informe uma letra: [F]Feminino | [M]Masculino :').upper()

if letra == 'F':
    print('\t\nSexo Feminino')
elif letra == 'M':
    print('\t\nSexo Masculino')
else:
    print('\t\nSexo inválido')
