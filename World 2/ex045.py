# -*- coding: utf-8 -*-
from random import randint
from time import sleep

# ex045 -> Programa para jogar Pedra, Papel e Tesoura!

op = ('pedra','papel','tesoura')

print('Seja bem vindo(a) ao Pedra, Papel, Tesoura!!')

jogada = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura'))
npc = randint(0,2)

print(f'Você Jogou {op[jogada]}')
sleep(2)
print(f'PC jogou {op[npc]}')

if (jogada==0 and npc==2) or (jogada==2 and npc==1) or (jogada==1 and npc==0):
    print(f'Parabéns, Você GANHOU!')
elif(npc==0 and jogada==2) or (npc==2 and jogada==1) or (npc==1 and jogada==0):
    print('Você Perdeu!')
else:
    print('Empate')
