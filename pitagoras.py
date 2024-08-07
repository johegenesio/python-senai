c1 = float(input('Coloque a medida de um cateto: '))
c2 = float(input('Coloque a medida do outro cateto: '))
h = (c1**2) + (c2**2)
h = h**(1/2)
print(f'O valor da hipotenusa é: {h}')
P = c1 + c2 + h
print(f'O valor do perimetro é: {P}')
A = (c1 * c2)/2
print(f'O valor da área é: {A}')