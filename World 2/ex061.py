# -*- coding: utf-8 -*-

# Programar uma P.A utilizando a estrutura 'while'

num = int(input('Qual é o primeiro termo da P.A? '))
raz = int(input('Qual é a razão da P.A? '))

cont = 10

while cont:
    print(f'{num}', end=' ')
    num += raz
    cont -= 1
print()
