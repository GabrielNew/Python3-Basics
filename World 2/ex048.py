# -*- coding: utf-8 -*-

'''
 ex048 -> Crie um programa que calcule a soma de todos os números ímpares
           e múltiplos de três no intervalo de 1 a 500.
'''

sum = cont = 0

for num in range(3,500,6):
    cont += 1
    sum += num

print(f'A soma dos {cont} valores vale {sum}')
