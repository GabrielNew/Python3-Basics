# -*- coding: utf-8 -*-

'''
 ex038 -> Escreva um programa que leia dois números e informe se:
          a) O primeiro é maior
          b) O segundo é maior
          c) Os dois são iguais
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro número é maior!')
elif num2 > num1:
    print('O segundo número é maior!')
else:
    print('Os dois números são iguais!')
