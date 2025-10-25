"""
Entrar com um nome e imprimir:
todo nome:
primeiro caractere:
último caractere:
do primeiro até o terceiro:
quarto caractere:
todos menos o primeiro:
os dois últimos:
"""

import os
os.system('cls')

nome = input('Digite um nome: ')

print(f'Nome: {nome} \nPrimeiro caractere: {nome[0]} \nÚltimo caractere: {nome[len(nome)-1]} \n Primeiro até o terceiro: {nome[0:3]} \nQuarto caractere: {nome[3]} \nTodos menos o primeiro: {nome[1:]} \nOs dois últimos: {nome[-2:]}')