# -*- coding: utf-8 -*-

'''
 ex042 -> Programa para saber se três segmentos pode formar um triângulo e ainda,
          falar que tipo de triângulo será formado.
'''

a = float(input('1° Lado: '))
b = float(input('2° Lado: '))
c = float(input('3° Lado: '))

if abs(a-b) < c < a+b and abs(a-c) < b < a+c and abs(b-c) < a < b+c:
    print('Os lados digitados PODEM formar um triângulo!')
    if a==b==c:
        print('Tipo Equilátero')
    elif a==b or b==c or c==a:
        print('Tipo Isósceles')
    else:
        print('Tipo Escaleno')
else:
    print('Os lados digitados NÃO PODEM formar um triângulo!')
