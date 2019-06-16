# -*- coding: utf-8 -*-

# ex025 -> Programa que lê o nome de uma pessoa, e diz se ela tem "SILVA" no nome

nome = str(input('Digite seu nome: ')).strip().upper()
nome = nome.split()

print(f'Tem Silva em seu nome? {"SILVA" in nome}')
