# -*- coding: utf-8 -*-

num = int(input('Digite um número para o cálculo do fatorial: '))
fat = 1

print(f'{num}! = ',end = '')
while num:
    fat *= num
    if num > 1:
        print(f'{num} x ', end='')
    else:
        print(f'{num} = ', end='')
    num -= 1

print(f'{fat}')
