# -*- coding: utf-8 -*-

# ex049 -> Programa para mostrar a tabuada de um número.

num = int(input('Digite um número para ver a sua tabuada: '))

for c in range(1,11):
    print(f'{num} x {c} = {num*c}')
