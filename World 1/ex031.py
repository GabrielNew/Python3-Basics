# -*- coding: utf-8 -*-

'''
 ex031 -> Escreva um programa que calcula o valor de uma viagem. Para viagens até
          200Km o valor por quilômetro é R$0.50. Já para viagens mais longas o
          valor é R$0.45.
'''

qtdkm = int(input('Digite a distância percorrida em KM: '))

if 0 < qtdkm <=200:
    preco = qtdkm * 0.50
else:
    preco = qtdkm * 0.45

print(f'Distância Total: {qtdkm}KM\nO valor da sua passagem será de R${preco:.2f}.')
