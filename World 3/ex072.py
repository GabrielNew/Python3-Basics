# -*- coding: utf-8 -*-

'''
 ex072 -> Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
          Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ( 'zero','um','dois','três','quatro','cinco','seis','sete',
            'oito','nove','dez','onze','doze','treze','quatorze','quinze',
            'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if 0<=num<=20:
        print(f'Você digitou o número {numeros[num]}')
        break
    else:
        print('Número inválido, tente novamente...')