# -*- coding: utf-8 -*-

'''
 ex022 -> Leia o nome completo de uma pessoa e faça:
          a) Mostre o nome com letras maiúsculas e minúsculas.
          b) Quantas letras tem ao todo(sem contar os espaços).
          c) Quantas letras tem o primeiro nome.
'''

nome = str(input('Por favor, Digite o seu nome completo: '))
totletras = len(nome.replace(' ',''))
prinome = nome.split(' ')

print(f'O seu nome em letras maiúsculas é: {nome.upper()}.')
print(f'O seu nome em letras minúsculas é: {nome.lower()}.')
print(f'O seu nome completo possui {totletras} letras.')
print(f'O seu primeiro nome possui {len(prinome[0])} letras.')
# print(f'O seu primeiro nome possui {nome.find(" ")} letras.')
