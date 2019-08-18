# -*- coding: utf-8 -*-

'''
  ex082 -> Crie um programa que vai ler vários números e colocar em uma lista. 
           Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
           respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

numeros = []
pares = []
impares = []
teste = True

while teste:
    num = int(input('Por favor, Digite um número: '))
    numeros.append(num)

    if num%2:
        impares.append(num)
    else:
        pares.append(num)

    op = str(input('Deseja inserir um outro número? [S/N]')).upper()

    if op == 'N':
        teste = False

print(f'A lista com todos os valores digitados é: {numeros}')
print(f'A lista com todos os valores pares é: {pares}')
print(f'A lista com todos os valores ímpares é: {impares}')
