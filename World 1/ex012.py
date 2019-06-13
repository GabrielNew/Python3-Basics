# -*- coding: utf-8 -*-

# ex012 -> Ler o preço de um produto e dar 5% de desconto.

preco = float(input('Qual o preço do produto? R$ '))

newprec = preco - (preco * 0.05)

print(f'O produto custava R${preco:.2f}.')
print(f'Mas com 5% de desconto fica R${newprec:.2f}.')
