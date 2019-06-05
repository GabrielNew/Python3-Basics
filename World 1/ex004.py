# -*- coding: utf-8 -*-
'''
ex004 -> Crie um programa que leia algo e mostre na tela seu tipo primitivo,
         e todas as informações possíveis sobre ele.
'''

var = input('Escreva Algo: ')
print(f'O tipo primitivo é: {type(var)}')
print(f'Só tem espaços? {var.isspace()}')
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f'É alfanumérico? {var.isalnum()}')
print(f'Está em maiúsculas? {var.isupper()}')
print(f'Está em minúsculas? {var.islower()}')
print(f'Está capitalizado? {var.istitle()}')
