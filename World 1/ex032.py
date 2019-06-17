# -*- coding: utf-8 -*-

# ex032 -> Ler um ano e informar ao usuário se ele é bissexto ou não.

from datetime import datetime

ano = int(input('Digite um ano: [0 - Para saber o ano atual] '))

if ano == 0:
    ano = datetime.now().year

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')
