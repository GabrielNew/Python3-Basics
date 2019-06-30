# -*- coding: utf-8 -*-

'''
 ex056 -> Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo, qual é o nome do homem
 mais velho e quantas mulheres têm menos de 20 anos.
'''

tot_idade = tot_mulher = maior_idade = media = 0
nome_midade = ''

for i in range(1,5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))

    tot_idade += idade
    if sexo in 'fF' and idade < 20:
        tot_mulher += 1
    if sexo in 'mM' and idade > maior_idade:
        nome_midade = nome

media = tot_idade/4

print(f'A média de idade do grupo é: {media:.1f}\nO homem mais velho se chama {nome_midade}')
print(f'O total de mulheres com menos de 20 anos é: {tot_mulher}')
