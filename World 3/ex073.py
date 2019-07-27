# -*- coding: utf-8 -*-

'''
  ex073 -> Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
  na ordem de colocação. Depois mostre:
  a) Os 5 primeiros times.
  b) Os últimos 3 colocados.
  c) Times em ordem alfabética. 
  d) Em que posição está o time do Bahia.
'''

times = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético MG', 'Athletico-PR', 'São Paulo',
        'Botafogo', 'Goiás', 'Corinthians', 'Grêmio', 'Bahia', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',  
        'Fluminense', 'Cruzeiro', 'Chapecoense', 'Avaí')

print('Os primeiros 4 colocadas são: ')
for i in range(0,4):
    print(f'{times[i]}', end = ' ')

print()
print('='*30)

print('Os últimos 3 colocados são: ')
i = -1
while i != -4:
    print(f'{times[i]}', end = ' ')   
    i += -1

print()
print('='*30)

print('Os times em ordem alfabética: ')
print(sorted(list(times)))

print('='*30)
print()

print(f'O Bahia EC está na colocação: {times.index("Bahia")+1}')

print('='*30)
