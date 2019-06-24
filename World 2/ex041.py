# -*- coding: utf-8 -*-
from datetime import datetime
'''
 ex041 -> Programa para ler o ano de nascimento de um nadador e mostrar a sua
          categoria
          a)até 9 anos = MIRIM                   b)até 14 anos = INFANTIL
          c)até 19 anos = JUNIOR                 d)até 25 anos = SÊNIOR
          e)Acima: MASTER
'''

ano_atual = datetime.now().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento

print(f'Você tem {idade} ano(s)')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
