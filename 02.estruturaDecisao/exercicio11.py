'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
    baseado no salário atual:
    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5% 
    Após o aumento ser realizado, informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento. '''
# -------------
# author: Paiva
# -------------

salario = float(input('Informe o salário: '))

if salario <= 280:
    valorAumento = (20 / 100) * salario
    percentual = '20%'
    novoSalario = valorAumento + salario
elif salario > 280 and salario <= 700:
    valorAumento = (15 / 100) * salario
    percentual = '15%'
    novoSalario = valorAumento + salario
elif salario > 700 and salario <= 1500:
    valorAumento = (10 / 100) * salario
    percentual = '10%'
    novoSalario = valorAumento + salario
else:
    valorAumento = (5 / 100) * salario
    percentual = '5%'
    novoSalario = valorAumento + salario

print('\nSalário antes do reajuste: ' + str(salario))
print('Percentual: ' + percentual)
print('Valor do aumento: ' + str(valorAumento))
print('Novo salário: ' + str(novoSalario))
