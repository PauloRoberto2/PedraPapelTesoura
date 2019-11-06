from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.25)
print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('computador venceu!')
elif computador == 1:
    if jogador == 0:
        print('computador venceu!')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu!')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('computador venceu!')
    elif jogador == 2:
        print('Empate')