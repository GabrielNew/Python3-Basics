# -*- coding: utf-8 -*-

'''
  ex081 ->  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
            A) Quantos números foram digitados.
            B) A lista de valores, ordenada de forma decrescente.
            C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []
teste = True

while teste:

    numeros.append(int(input('Digite um Número: ')))
    op = str(input('Deseja inserir outro número na lista? [S/N] ')).upper()
    if op == 'N':
        teste = False
    
print(f'A quantidade de elementos na lista é: {len(numeros)}')
print(f'Os valores ordenados de forma decrescente são: {sorted(numeros, reverse=True)}')

if 5 in numeros:
    print('O valor 5 está presente na lista!')
else:
    print('O valor 5 não está presente na lista!')
