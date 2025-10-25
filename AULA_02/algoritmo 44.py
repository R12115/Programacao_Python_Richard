import os
os.system('cls')
import math as m

numero = int(input('Digite um numero: '))
base = int(input('Digite um numero: '))

logaritmo = m.log(numero, base)

print(f'O logaritmo de {numero} na base {base} é {logaritmo}')