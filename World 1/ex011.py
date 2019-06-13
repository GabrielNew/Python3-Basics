# -*- coding: utf-8 -*-

'''
 ex011 -> Calcular a área de uma parede retangular e a quantidade necessária,
          em litros, de tinta para pinta-lá. Um litro de tinta pinta 2m².
'''

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = (alt * lar)
ltint = area/2

print(f'A parede tem uma área de {area:.3f}m². ')
print(f'Será necessário {ltint:.2f} litros de tinta, para a pintura.')
