# -*- coding: utf-8 -*-

# ex043 -> Programa para calcular o IMC de uma pessoa.

peso = float(input('Qual é o seu peso(KG)? '))
altura = float(input('Qual é a sua altura? '))

imc = peso/(altura**2)

print(f'Com o IMC de {imc:.1f} ', end = '')
if imc < 18.5:
    print('você está ABAIXO DO PESO.')
elif imc < 25:
    print('você está com o PESO IDEAL.')
elif imc < 30:
    print('você está com SOBREPESO.')
elif imc < 40:
    print('você está com OBESIDADE.')
else:
    print('você está com OBESIDADE MÓRBIDA.')
