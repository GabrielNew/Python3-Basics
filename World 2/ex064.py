# -*- coding: utf-8 -*-

# ex064 -> Programa para contar quantos valores foram digitados e a soma entre eles

qtd = soma = 0

while True:
    num = int(input('Digite um número[999 para encerrar]: '))
    if num != 999:
        qtd += 1
        soma += num
    else:
        break

print(f'A quantidade de números digitados foi {qtd}, e a soma entre eles vale {soma}')
