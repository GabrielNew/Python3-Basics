# -*- coding: utf-8 -*-

# ex052 -> Crie um programa para informar se um número é primo ou não

num = int(input('Digite um número: '))
cont = 0

for i in range(1, num+1):
    if num%i==0:
        cont += 1

print(f'O número {num}', end = ' ')
if cont==2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
