# -*- coding: utf-8 -*-

'''
  ex084 -> Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
           A) Quantas pessoas foram cadastradas.
           B) Uma listagem com as pessoas mais pesadas.
           C) Uma listagem com as pessoas mais leves.
'''

pessoa = []
total = []
teste = True

while teste:
    pessoa.append(str(input('Digite seu nome: ')))
    pessoa.append(float(input('Digite seu peso em KG: ')))

    if len(total) == 0:
        pesado = leve = pessoa[1]
    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]

    total.append(pessoa.copy())
    pessoa.clear()

    op = str(input('Deseja Continuar? [S/N]')).upper()
    if op == 'N':
        teste = False

print(f'O total de pessoas cadastradas foi de: {len(total)}')
print(f'O maior peso foi o de {pesado}Kg, pessoas:', end = ' ')
for i in range(len(total)):
    if total[i][1] == pesado:
        print(total[i][0], end = ' ')

print()

print(f'O menor peso foi o de {leve}Kg, pessoas:', end = ' ')
for i in range(len(total)):
    if total[i][1] == leve:
        print(total[i][0], end = ' ')
