# -*- coding: utf-8 -*-

# ex053 -> Programa para identificar se um texto/palavra é um palíndromo

texto = str(input('Digite uma frase: ')).replace(' ','')

inverso = texto[::-1]

if inverso == texto:
    print('Palíndromo')
else:
    print('Não é Palíndromo')
