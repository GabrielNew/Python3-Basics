# -*- coding: utf-8 -*-

# ex017 -> Crie um programa que calcule e mostre a hipotenusa de um triângulo.

catop = float(input('Qual é o comprimento do cateto oposto? '))
catad = float(input('Qual é o comprimento do cateto adjacente? '))

hip = pow( (pow(catop, 2) + pow(catad,2) ), 1/2)

# hip = math.hypot(catop,catad) com a importação da classe Math
# hip = (catop**2 + catad**2) ** (1/2) (O operador (**) eleva)

print(f'O valor da hipotenusa do triângulo é: {hip:.2f}')
