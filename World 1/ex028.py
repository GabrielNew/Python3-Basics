# -*- coding: utf-8 -*-


'''
 ex028 -> Escreva um programa onde o computador "pensa" em um número entre 0 e 5
          e peça para o usuário tentar adivinhar. Escrever ao final se o usuário
          ganhou ou perdeu.
'''

from random import randint
from time import sleep
import os


npc = randint(0,5)

print('Pensei em um número entre 0 e 5...')
sleep(3)
os.system('clear')
user = int(input('Tente adivinhar em qual número em pensei: '))

if user != npc:
    print(f'Você perdeu, eu pensei no número {npc} e você chutou o número {user}.')
else:
    print('Parabéns, você venceu!')
