# -*- coding: utf-8 -*-

'''
 ex040 -> Programa que lê duas notas e informe a média do aluno e sua situação.
          a) Média maior ou igual a 7.0 = APROVADO
          b) Média entre 5.0 e 6.9 = RECUPERAÇÃO
          c) Média menor que 5.0 = REPROVADO
'''

nota1 = float(input('Digite a sua 1º nota: '))
nota2 = float(input('Digite a sua 2º nota: '))
media = (nota1+nota2)/2.0

print(f'Média = {media:.1f}')

if media >= 7.0:
    print('APROVADO')
elif media < 5.0:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')
