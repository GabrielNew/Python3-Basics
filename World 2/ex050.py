# -*- coding: utf-8 -*-

'''
 ex050 -> Crie um programa que leia seis números e faça um soma de todos os pares.
          Caso o número lido seja ímpar, desconsidere-o.
'''

sum = 0

for c in range(1,7):
    num = int(input('Digite um número: '))

    if num%2 == 0:
        sum += num

print(f'A soma dos número pares digitados vale {sum}')
