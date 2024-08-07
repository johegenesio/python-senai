salario = float(input('Qual seu salário: '))
if salario <= 1903.98:
    print('Você não tem imposto')
elif salario <= 2826.65:
    imp = ((7.5/100)*salario)-142.80
    print(f'Você tem um imposto de: {imp:.2f}')
elif salario <= 3751.05:
    imp = ((15/100)*salario)-354.80
    print(f'Você tem um imposto de: {imp:.2f}')
elif salario <= 4664.68:
    imp = ((22.5/100)*salario)-636.13
    print(f'Você tem um imposto de: {imp:.2f}')
else:
    imp = ((27.5/100)*salario)-869.36
    print(f'Você tem um imposto de: {imp:.2f}')