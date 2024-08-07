i = int(input('Digite um número: '))
n = 0
for n in range (i):
    print(n)
print(i)

#################

c = ""
for c in 'Lucas':
    print(c)

##################

c= "Lucas"
print(c[3])

###################

nome=str(input('Digite seu nome: '))
print(nome[::-1])

for j in range(len(nome),0,-1):
    print(nome[j-1])

nome_invertido=''

for inverte in nome:
    nome_invertido = inverte + nome_invertido
print(f'Seu nome é invertido é {nome_invertido}')

####################