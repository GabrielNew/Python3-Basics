# -*- coding: utf-8 -*-

'''
 ex071 -> Crie um programa que simule o funcionamento de um caixa eletrônico.
          No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
          e o programa vai informar quantas cédulas de cada valor serão entregues.
'''

valor = int(input('Qual valor você deseja sacar? R$'))
notas = (50,20,10,1)

for i in notas:
    qtd = valor // i
    if qtd>0:
        print(f'A quantidade de cédulas de {i} é {qtd}')
        valor -= qtd*i
