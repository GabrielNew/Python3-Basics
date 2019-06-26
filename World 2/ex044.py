# -*- coding: utf-8 -*-

'''
 ex044 -> Elabore um programa que calcule o valor a ser pago por um produto,
          considerando seu preço normal e forma de pagamento:
          a) Á vista dinheiro/cheque = 10% de desconto
          b) Á vista no cartão = 5% de desconto
          c) Em até 2x no cartão = preço normal
          d) 3x ou mais no cartão = 20% de juros
'''
valor = parcelas = 0

preco = float(input('Qual o valor do produto? R$'))

print("""
    1 - Á vista(Dinheiro/Cheque)
    2 - Á vista Cartão
    3 - Parcelado 2 vezes no Cartão
    4 - Parcelado 3 ou mais vezes no cartão
    """)

op = int(input('Qual é a forma de pagamento?'))

if op==1:
    valor = preco - (preco * 0.10)

elif op==2:
    valor = preco - (preco * 0.05)

elif op==3:
    valor = preco
    parcela = preco / 2
    print(f'Será pago em 2 parcelas de {parcela:.2f}', end=' ')

elif op==4:
    qtdpa = int(input('Qual o número de parcelas? '))
    if qtdpa >=3:
        valor = preco + (preco * 0.20)
        parcela = valor / qtdpa
        print(f'Será pago em {qtdpa} parcelas de {parcela:.2f}', end=' ')
    else:
        print('Erro no número de parcelas')
        
else:
    print('Opção Inválida')

print(f'Seu produto de R${preco:.2f} irá custar agora R${valor:.2f}')
