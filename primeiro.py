name = input("Digite seu nome: ").title().strip()
print(f"Olá, {name}")

def soma (num1, num2):
    return round(num1 + num2,4)

def main ():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = (num1 + num2)

    print(soma)

main()