# -*- coding: utf-8 -*-

'''
 ex034 -> Escreva um programa que pergunte qual o salário de um funcionário.
          Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
          Para os inferiores ou iguais, o aumento é de 15%.
'''

aumento = 0
sal = float(input('Salário: '))

# novosal = (sal + (sal*0.15)) if sal <= 1250.0 else sal + (sal*0.10)

if sal <= 1250.0:
    aumento = 0.15
else:
    aumento = 0.10

novosal = sal + (sal * aumento)

print(f'O antigo salário era de R${sal:.2f}\nSeu novo salário tem o valor de R${novosal:.2f}')
print(f'A porcentagem de aumento salarial foi de {aumento:.2f}%')
