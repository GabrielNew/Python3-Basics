# -*- coding: utf-8 -*-

# ex055 -> Programa para informar o maior e o menor peso lido, entre 5 pessoas

maior_peso = menor_peso = 0

for p in range(1,6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if peso > maior_peso or p == 1:
        maior_peso = peso
    if peso < menor_peso or p == 1:
        menor_peso = peso

print(f'O maior peso {maior_peso:.2f}kg\nO menor peso {menor_peso:.2f}kg')
