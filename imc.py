peso=float(input('Digite seu peso em KG (exemplo: 50): '))
altura=float(input('Digite sua altura em metros (exemplo: 1.90): '))
calc=peso/(altura**2)
if (calc < 18.5):
    print(f'Abaixo do peso ideal (seu IMC é {calc:.2f})')
elif (calc < 25):
    print(f'Peso ideal (seu IMC é {calc:.2f})')
elif (calc < 30):
    print(f'Excesso de peso (seu IMC é {calc:.2f})')
elif (calc < 35):
    print(f'Obesidade grau I (seu IMC é {calc:.2f})')
elif (calc < 40):
    print(f'Obesidade grau II (seu IMC é {calc:.2f})')
else:
    print(f'Obesidade grau III (seu IMC é {calc:.2f})')