# -*- coding: utf-8 -*-

# ex024 -> Programa que lê o nome de uma cidade, e diz se o primeiro nome é 'Santo'

local = str(input('Digite o nome de uma cidade: ')).strip(' ')
city = local.upper().split(' ')
print(city[0] == 'SANTO')
