"""
Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a
diagonal.
"""
import os
os.system('cls')
import math as m


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))


D = m.sqrt(a**2 + b**2 + c**2)

print(round(D,2))