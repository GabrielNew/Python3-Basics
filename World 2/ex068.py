# -*- coding: utf-8 -*-

from random import randint

# ex068 -> Programa para jogar Par ou Ímpar com o computador

tot_vit = 0
op = ' '

while True:
    player = int(input('Qual número você deseja jogar? '))

    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]

    pc = randint(0,10)

    print(f'Você jogou {player}, o PC jogou {pc}...')

    if op == 'P':
        if (player + pc)%2 == 0:
            print('Parabéns você ganhou deu PAR, vamos jogar mais...')
            tot_vit += 1
        else:
            print('Infelizmente você perdeu!')
            break
    else:
        if (player + pc)%2 != 0:
            print('Parabéns você ganhou deu ÍMPAR, vamos jogar mais...')
            tot_vit += 1
        else:
            print('Infelizmente você perdeu!')
            break

print(f'Você ganhou um total de {tot_vit} vezes!')
