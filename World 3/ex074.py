# -*- coding: utf-8 -*-

from random import randint

'''
  ex074 -> Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
  Depois disso, mostre os números gerados e também indique o menor e o maior valor na tupla.
'''

elementos = ( randint(0,10), randint(0,10), randint(0,10),
              randint(0,10), randint(0,10) )

print('Valores Gerados = ', end = '')
print(elementos)
print(f'O maior valor é o {max(elementos)}')
print(f'O menor valor é o {min(elementos)}')