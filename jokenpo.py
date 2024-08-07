import random
jogadas = ('papel', 'tesoura', 'pedra')
p1 = input('Jogue papel, tesoura ou pedra: ').lower()
while p1 not in jogadas:
    p1 = input('Jogue papel, tesoura ou pedra: ')
npc = jogadas[random.randrange(3)]
print(f'O computador jogou {npc}')
if p1 == npc:
    print('Empate')
else:
    if p1 == 'pedra':
        if npc == 'papel':
            print('Você perdeu')
        else:
            print('Você ganhou')
    if p1 == 'papel':
        if npc == 'tesoura':
            print('Você perdeu')
        else:
            print('Você ganhou')
    if p1 == 'tesoura':
        if npc == 'pedra':
            print('Você perdeu')
        else:
            print('Você ganhou')