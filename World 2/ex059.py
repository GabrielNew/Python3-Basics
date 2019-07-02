# -*- coding: utf-8 -*-


'''
 ex059 -> Crie um programa que leia dois valores e mostre um menu na tela:
          [ 1 ] somar
          [ 2 ] multiplicar
          [ 3 ] maior
          [ 4 ] novos números
          [ 5 ] sair do programa
          Seu programa deverá realizar a operação solicitada em cada caso.
'''

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

while True:
    print("""
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos Números
          [5] - Sair do Programa
          """)
    op = int(input('Qual operação você deseja realizar? '))
    if op == 1:
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    elif op == 2:
        multi = num1 * num2
        print(f'{num1} * {num2} = {multi}')
    elif op == 3:
        if num1>num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número é o {maior}')
    elif op == 4:
        print('Digite novos valores...')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif op == 5:
        print('Obrigado por Utilizar este programa!!')
        break
    else:
        print('Opção Inválida, Tente Novamente...')
