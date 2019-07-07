# -*- coding: utf-8 -*-

'''
 ex065 -> Programa para ler vários números e no final mostrar a media, o maior
           e o menor entre todos os valores digitados.
'''

op = ' '
media = qtd = maior = menor = 0

while op != 'N':
    num = int(input('Digite um número: '))
    qtd += 1
    media += num
    if maior < num or qtd == 1:
        maior = num
    if num < menor or qtd == 1:
        menor = num
    op = str(input('Deseja continuar? [S/N]')).upper()

print(f'A quantidade de números digitados foi {qtd}\nA média foi de {media/qtd:.2f}')
print(f'O maior valor foi o de {maior} e o menor foi o {menor}')
