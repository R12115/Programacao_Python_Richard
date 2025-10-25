import os
os.system('cls')
import math

# Entrar com um número e imprimir o logaritmo desse número na base 10.

numero = int(input("Digite um numero"))

log10 = math.log10(numero)

print(f'O log10 de {numero} é {log10}')