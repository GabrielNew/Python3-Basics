# -*- coding: utf-8 -*-

# ex035 -> Crie um programa para saber se as medidas digitadas pelo usuário formam um triângulo

a = float(input('1° Lado: '))
b = float(input('2° Lado: '))
c = float(input('3° Lado: '))

if abs(a-b) < c < a+b and abs(a-c) < b < a+c and abs(b-c) < a < b+c:
    print('Os lados digitados PODEM formar um triângulo!')
else:
    print('Os lados digitados NÃO PODEM formar um triângulo!')
