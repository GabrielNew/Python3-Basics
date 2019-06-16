# -*- coding: utf-8 -*-

'''
 ex026 -> Crie um programa que leia uma frase e diga:
          a) Quantas vezes aparece a letra 'A'
          b) Em que posição "A" apareceu pela primeira vez
          c) Em que posição "A" apareceu pela última vez
'''

frase = str(input('Digite sua frase: ')).strip().upper()

print(f'A letra "A" apareceu {frase.count("A")} vezes.')
print(f'A primeira vez que "A" aparece é na posição {frase.find("A")+1}.')
print(f'A última vez que "A" aparece é na posição {frase.rfind("A")+1}.')
