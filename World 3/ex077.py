# -*- coding: utf-8 -*-

'''
  ex077 -> Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
           Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('LINGUAGEM','PROGRAMACAO','ESTUDAR','PESQUISA','PROGRAMA',
            'PYTHON','JAVA','EXERCICIOS')


for i in palavras:
    print('\n')
    print(f'{i}', end = ' = ')
    for pos in range(len(i)):
        if i[pos].upper() in 'AEIOU':
            print(f'{i[pos]}', end = ' ')