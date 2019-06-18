# -*- coding: utf-8 -*-

# ex033 -> Crie um programa que leia três números e diga qual é o maior e o menor

n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))

num = [n1,n2,n3]

print(f'O maior valor é o {max(num)}!')
print(f'O menor valor é o {min(num)}!')
