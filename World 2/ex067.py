# -*- coding: utf-8 -*-

'''
 ex067 -> Mostrar a abudada para qualquer valor positivo, digitado pelo usuário.
          Caso contrário o programa encerra.
'''

while True:
    num = int(input('Qual o valor para mostrar a tabuada? '))

    if num>0:
        print(f'Tabuada de {num}')
        for i in range(1,11):
            print(f'{num} x {i} = {num*i}')
    else:
        break
