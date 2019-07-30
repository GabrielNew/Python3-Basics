# -*- coding: utf-8 -*-

'''
  ex075 -> Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
           No final, mostre:
           A) Quantas vezes apareceu o valor 9.
           B) Em que posição foi digitado o primeiro valor 3.
           C) Quais foram os números pares.
'''

nums = ()
pares = ()
totnove = 0

for i in range(0,4):
    elemento = int(input('Digite um Número: '))
    nums += (elemento,)   

for i in nums:
    if i == 9:
        totnove += 1
    if i%2 == 0:
        pares += (i,)

print(f'O total de 9 digitados foi: {totnove}')
print(f'Os números pares digitados são {pares}')
if 3 in nums:
    print(f'A posição do primeiro número 3 é: {nums.index(3)}')
else:
    print('Número 3 não está presente na tupla...')
