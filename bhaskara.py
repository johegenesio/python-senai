a = float(input('Coloque o valor de a: '))
b = float(input('Coloque o valor de b: '))
c = float(input('Coloque o valor de c: '))

bhask = b**2 - 4 * a * c
print(f'O valor de Delta é {bhask}')
if bhask < 0:
    print('Não tem raiz real')
elif bhask == 0:
    calc = (-b + bhask**(1/2)) / (2 * a)
    print(calc)
else:
    calc = (-b + bhask**(1/2)) / (2 * a)
    calc2 = (-b - bhask**(1/2)) / (2 * a)
    print(f'Primeiro x = {calc} e segundo x = {calc2}')