# -*- coding: utf-8 -*-

from math import sin, cos, tan, radians

# ex018 -> Programa para calcular a tangente, cosseno e o seno de um ângulo.

ang = float(input('Digite um Ângulo: '))

seno = sin(radians(ang))
cos = cos(radians(ang))
tag = tan(radians(ang))

print(f'O ângulo de {ang:.2f} possui: ')
print(f'Seno: {seno:.2f}\nCosseno: {cos:.2f}\nTangente: {tag:.2f}')
