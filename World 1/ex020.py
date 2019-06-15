# -*- coding: utf-8 -*-

from random import shuffle
from time import sleep

# ex020 -> Programa para sorter a ordem de apresentação.

alunos = []

for i in range(0,4):
    alunos.append(str(input(f'Qual o nome do {i+1}° aluno: ')))

print('Sorteando Ordem...')
shuffle(alunos)
sleep(2)

print(f'A ordem de apresentação é {alunos}')
