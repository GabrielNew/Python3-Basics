# -*- coding: utf-8 -*-
'''
 ex023 -> Programa que lê um número de 0 a 9999 e mostra os números separados
          em unidade, dezena, centena e milhar
'''

num = int(input('Digite um número entre 0 e 9999: '))

unidade = num % 10
dezena = (num % 100) // 10
centena = (num % 1000) // 100
milhar = (num % 10000) // 1000

print(f'Número Digitado: {num}')
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')
