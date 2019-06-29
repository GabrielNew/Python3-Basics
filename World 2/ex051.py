# -*- coding: utf-8 -*-

# ex051 -> Programa para mostrar os 10 primeiros termos de uma PA

ptermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

for c in range(1,11):
    print(f'{ptermo}', end = ' ')
    ptermo += razao
print('\n')
