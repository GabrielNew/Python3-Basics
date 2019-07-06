# -*- coding: utf-8 -*-

# Programar uma P.A utilizando a estrutura 'while'

num = int(input('Qual é o primeiro termo da P.A? '))
raz = int(input('Qual é a razão da P.A? '))

cont = 10
qtd_termos = 0

while cont:
    print(f'{num}', end=' ')
    num += raz
    cont -= 1
    qtd_termos += 1
    if cont==0:
        print('Stop!')
        cont = int(input('Deseja mostrar mais quantos termos: '))
print(f'Ao total foram mostrados {qtd_termos} termos da P.A!')
