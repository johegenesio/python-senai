menu = ('S', 'N', 'R')
p1 = input('Quer começar? S/N')
while p1 not in menu:
    print(float(input('Coloque S/N: ')))
    if menu == 'S':
        print(float(input('Coloque um número')))