# -*- coding: utf-8 -*-
from datetime import datetime

'''
 ex039 -> Programa para ler a data de nascimento de uma pessoa, e informar se
          ela deve, ou não se alistar
'''

nascimento = int(input('Em que ano você nasceu? '))

ano_atual = datetime.now().year
idade =  ano_atual - nascimento

print(f'Você tem {idade} anos')
if idade < 18:
    aux = 18 - idade
    print(f'Ainda falta(m) {aux} ano(s) para o seu alistamento, que será em {ano_atual + aux}')
elif idade > 18:
    aux = idade - 18
    print(f'O Alistamento deve ter sido realizado há {aux} ano(s) atrás, em {ano_atual - aux}')
else:
    print('Realize o alistamento militar imediatamente')
