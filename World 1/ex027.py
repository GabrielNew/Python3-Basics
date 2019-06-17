# -*- coding: utf-8 -*-

# ex027 -> Leia o nome completo de uma pessoa e mostre o primeiro e o último nome.

nome = str(input('Por favor, Digite o seu nome completo: ')).strip()

pri = nome.find(' ')
ult = nome.rfind(' ')

print(f'O seu primeiro nome é: {nome[0:pri]}')
print(f'O seu último nome é: {nome[ult+1:]}')
