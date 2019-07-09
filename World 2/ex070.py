# -*- coding: utf-8 -*-

'''
 ex070 ->  Crie um programa que leia o nome e o preço de vários produtos.
           O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
           A) qual é o total gasto na compra.
           B) quantos produtos custam mais de R$1000.
           C) qual é o nome do produto mais barato.
'''

tot_compra = tot_produ_mil = menor_preco = 0
while True:
    op = ' '
    nome = str(input('Nome do Produto: '))
    valor = float(input(f'Qual é o preço da {nome}: R$'))

    if valor > 1000:
        tot_produ_mil += 1
    elif valor < menor_preco or tot_compra == 0:
        menor_preco = valor
        nome_menor = nome

    tot_compra += valor
    while op not in 'SN':
        op = str(input('Deseja comprar mais? - [S/N]')).upper().strip()[0]
    if op == 'N':
        break

print('\n')
print(f'Valor total: R${tot_compra:.2f}')
print(f'Quantidade de produtos acima de R$1.000: {tot_produ_mil}')
print(f'O produto mais barato foi {nome_menor}, custando R${menor_preco:.2f}')
