# -*- coding: utf-8 -*-

'''
  ex078 ->  Crie um programa que leia 5 valores numéricos e guarde-os em uma lista. 
            No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''

numeros = []
pos_maior = []
pos_menor = []
c = 0

while c<5:
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))
    c += 1

maior_num = max(numeros)
menor_num = min(numeros)

for pos, num in enumerate(numeros):
    if num == maior_num:
        pos_maior.append(pos)
    if num == menor_num:
        pos_menor.append(pos)

print(f'O maior número é o {maior_num}, presente em {pos_maior}')
print(f'O menor número é o {menor_num}, presente em {pos_menor}')
