# -*- coding: utf-8 -*-

'''
  ex083 -> Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
           Seu aplicativo deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta.
'''

parenteses = []
teste = True

exp = str(input('Digite uma expressão: '))

for i in exp:
    if i == '(':
        parenteses.append(i)
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            resultado = 'Expressão Inválida'
            teste = False
            break
                     
if teste:
    resultado = 'Expressão Válida' if (len(parenteses) == 0) else 'Expressão Inválida'

print(resultado)
