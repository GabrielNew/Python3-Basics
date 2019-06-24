# -*- coding: utf-8 -*-

'''
 ex037 -> Escreva um programa que leia um número e pergunte ao usuário, para qual
          base ele quer converter o número. 1 - Binário 2 - Octal e 3 - Hexadecimal
'''

num = int(input('Digite um número: '))
print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
op = int(input(f'Para qual base deseja transformar o {num}?'))

if op == 1:
    print(f'{bin(num)}')
elif op == 2:
    print(f'{oct(num)}')
elif op == 3:
    print(f'{hex(num)}')
else:
    print('Opção Inválida...')
