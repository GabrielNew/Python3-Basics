# -*- coding: utf-8 -*-

'''
  ex079 ->  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
            Caso o número já exista lá dentro, ele não será adicionado. 
            No final, serão exibidos todos os valores únicos digitados, em ordem crescente.  
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
