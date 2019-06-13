# -*- coding: utf-8 -*-

# ex008 -> Ler um valor em metros e, realizar uma conversão entre as principais medidas.

medidas = ('km','hm','dam','m','dm','cm','mm')
inicio = 0.001
metros = float(input('Digite um valor em metros: '))

print(f'{metros}m vale:')
for c in range(len(medidas)):
    if c != 3:
        print(f'{metros * inicio:.3f} {medidas[c]}')
        inicio *= 10
