# -*- coding: utf-8 -*-


'''
 ex057 -> Crie um programa que leia o sexo de uma pessoa. Só aceite os valores 'M' ou 'F'.
          Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()

    if sexo not in 'MF':
        print('Dado Inválido, Digite Novamente... ')
    else:
        print(f'Sexo {sexo} registrado!')
        break
