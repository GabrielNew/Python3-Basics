# -*- coding: utf-8 -*-

'''
  ex076 ->  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços. 
            No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

itens = ('Caderno', 20.0,
         'Lápis', 1.50,
         'Caneta', 2.00,
         'Borracha', 0.50,
         'Lapiseira', 5.00,
         'Pontas', 3.00)

for item in range(0, len(itens)):
    if item%2 == 0:
        print(f'{itens[item]:.<30}', end = '')
    else:
        print(f'R${itens[item]:.2f}')

