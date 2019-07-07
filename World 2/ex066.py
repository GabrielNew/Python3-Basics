# -*- coding: utf-8 -*-

# ex066 -> Programa para mostrar a soma, a média e a quantidade de valores digitados

qtd = soma = media = 0

while True:
    num = int(input('Digite um número[999 para encerrar]: '))
    if num != 999:
        qtd += 1
        soma += num
    else:
        break

print(f'A quantidade de números digitados foi {qtd}')
print(f'A média vale: {soma/qtd}')
print(f'A soma vale: {soma}')
