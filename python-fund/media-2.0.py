qtdd = int(input('Quantas notas irá digitar: '))
soma = 0
for calc in range (0,qtdd,1):
    soma = soma + float(input('Digite a nota: '))
print(f'{soma/qtdd:.2f}')