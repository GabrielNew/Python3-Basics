# -*- coding: utf-8 -*-

'''
 ex069 -> Crie um programa que leia a idade e o sexo de várias pessoas. Depois mostre:
          a) Quantas pessoas tem mais de 18 anos
          b) Quantos homens foram cadastrados
          c) Quantas mulheres tem menos de 20 anos
'''

tot_pessoas_maior = tot_mulher_20 = tot_homem = 0

while True:
    sexo = op = ' '
    idade = int(input('Digite sua idade: '))

    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo - [M/F]: ')).upper().strip()[0]

    if idade > 18:
        tot_pessoas_maior += 1
    if sexo == 'M':
        tot_homem += 1
    elif sexo == 'F' and idade < 20:
        tot_mulher_20 += 1

    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot_pessoas_maior}')
print(f'Total de homens cadastrados: {tot_homem}')
print(f'Total de mulheres com menos de 20 anos: {tot_mulher_20}')
