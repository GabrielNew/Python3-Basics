# -*- coding: utf-8 -*-

# ex054 -> Programa para informar quantas pessoas são maiores e menores de idade

from datetime import datetime

ano_atual = datetime.today().year
totmaior = totmenor = 0

for i in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {i}° pessoa? '))
    if ano_atual - nasc >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f'Total de maiores de Idade: {totmaior}\nTotal de menores de Idade: {totmenor}')
