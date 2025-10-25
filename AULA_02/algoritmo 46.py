import os
os.system('cls')

"""
Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima
o novo saldo, considerando o reajuste de 1%.
"""

Saldo = float(input("Digite o saldo da aplicação: "))

reajuste = 0.01
resultado = Saldo + (Saldo * reajuste)

print(resultado)