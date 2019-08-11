# -*- coding: utf-8 -*-

'''
  ex080 ->  Crie um programa onde o usuário possa digitar valores numéricos e cadastre-os em uma lista, 
            já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

numeros = []
tam = 0
op = True

while True:
    num = int(input('Digite um número: '))

    if num not in numeros:
        if len(numeros) == 0:
            numeros.append(num)
        else:
            for i in range(len(numeros)):
                if num < numeros[i]:
                    numeros.insert(i, num)
                    break
                else:
                    tam += 1

                if tam == len(numeros):
                    numeros.append(num)
            tam = 0
    else:
        print('A lista já possui este número')
    op = str(input('Deseja adicionar mais um número? [S/N] ')).upper()
    if op == 'N':
        op = False
        break


print(numeros)
