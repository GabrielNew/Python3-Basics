# -*- coding: utf-8 -*-

'''
 ex029 -> Escreva um programa que leia a velocidade de um carro. Se a velocidade
          ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.
          A multa custa R$ 7.00 por Km acima do limite.
'''

vel = int(input('Qual é a velocidade do carro: '))

if vel > 80:
    print('Você será multado! Limite de velocidade é 80Km/h.')
    valor = (vel - 80) * 7
    print(f'A multa será no valor de R$ {valor:.2f}')
else:
    print('Você está dentro dos limites de velocidade!')
