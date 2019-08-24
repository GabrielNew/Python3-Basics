# -*- coding: utf-8 -*-

'''
  ex085 -> Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
           lista única que mantenha separados os valores pares e ímpares. 
           No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]

for i in range(1,8):
    num = int(input(f'{i}° - Número: '))

    if num%2:
        numeros[1].append(num)
    else:
        numeros[0].append(num)

print(f'Os numeros pares: {sorted(numeros[0])}')
print(f'Os numeros ímpares: {sorted(numeros[1])}')