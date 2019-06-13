# -*- coding: utf-8 -*-

'''
 ex015 -> Calcular o valor de um aluguel de carro. Sabendo que a diária custa R$60.00
          e 0,15 por KM rodado.
'''

qtd_dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km rodou? '))

valor = (qtd_dias*60.0) + (km * 0.15)

print(f'Você usou o carro por {qtd_dias} dias e rodou {km}.')
print(f'O valor a pagar é de R${valor:.2f}.')
