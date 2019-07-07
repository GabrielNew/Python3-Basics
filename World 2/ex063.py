# -*- coding: utf-8 -*-

# ex063 -> Programa para mostrar a sequência de Fibonacci

qtd = int(input("Quantos termos da sequência de Fibonacci você deseja ver? "))
ant = atual = 0
prox = 1

while qtd:
    print(f'{atual}', end = ' ')
    ant = prox
    prox = atual
    atual = ant + prox
    qtd -= 1
    
print('\n')
