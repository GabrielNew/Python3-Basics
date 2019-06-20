# -*- coding: utf-8 -*-

'''
 ex036 -> Escreva um programa para aprovar o emprestimo bancário para a compra
          de uma casa. Pergunte o valor da casa, o salário do comprador e em
          quantos anos deseja pagar. A prestação mensal não pode exceder 30%
          do salário, caso contrário, o empréstimo será negado.
'''

ValorCasa = float(input('Qual é o valor da casa? R$'))
Salario = float(input('Qual é o seu salário? R$'))
QtdAnos = int(input('Em quantos anos deseja pagar? '))

Parcela = ValorCasa / (QtdAnos*12)

print(f'Valor da casa: R${ValorCasa:.2f}\nParcela Mensal: R${Parcela:.2f} durante {QtdAnos} anos!')

if Parcela > Salario * 0.30:
    print(f'Empréstimo Negado!')
else:
    print(f'Empréstimo Autorizado!')
