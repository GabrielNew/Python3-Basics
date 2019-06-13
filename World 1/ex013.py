# -*- coding: utf-8 -*-

# ex013 -> Ler o salario de um funcionário e dar 15% de aumento.

sal = float(input('Qual é o salário do funcionário? R$ '))

novsal = sal + (sal * 0.15)

print(f'O funcionário ganhava {sal:.2f}, mas com o aumento de 15% passa a ganhar {novsal:.2f}')
