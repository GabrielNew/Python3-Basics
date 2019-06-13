# -*- coding: utf-8 -*-

# ex010 -> transformar uma quantidade em reais para dólares.

money = float(input('Quantos dinheiro em reais você tem? R$ '))
dolar = money/3.88 # cotação do dólar dia 08/06/2019
print(f'Você tem em dólares {dolar:.2f}')
