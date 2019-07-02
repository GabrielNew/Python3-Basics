# -*- coding: utf-8 -*-

from random import randint
from time import sleep
import os

'''
 ex058 -> Crie um programa onde o computador "pensa" em um número e o usuário tem
          que adivinhar. Ao final mostrar quantas tentativas foram necessárias.
'''

npc = randint(0,10)
tentativas = 0

print('Jogo da Adivinhação')
sleep(2)
os.system('clear')

print('Acabei de pensar em um número entre 0 e 10, tente adivinhar...')
sleep(2)

while True:
    palpite = int(input('Qual é o seu palpite? '))

    if palpite < npc:
        print('Maior...')
        tentativas += 1
    elif palpite > npc:
        print('Menor...')
        tentativas += 1
    else:
        print(f'Parabéns, você acertou. Eu pensei exatamente no número {npc}!')
        print(f'Você precisou de {tentativas} tentativas.)
        break
