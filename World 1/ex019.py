# -*- coding: utf-8 -*-

from random import randint, choice

# ex019 -> Sortear um aluno para apagar o quadro.

nomes = []

for i in range(0,4):
    nomes.append(str(input('Digite um nome: ')))

aluno = randint(0,4)
# aluno = choice(nomes) usando o método choice

print(f'O aluno(a) escolhido(a) foi {nomes[aluno]}')
