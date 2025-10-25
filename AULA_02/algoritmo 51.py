"""
Entrar com o raio de um circulo e imprimir a seguinte saída:
perimetro:
area:
"""

import os
os.system('cls')
import math as m

raio = float(input('Digite o Raio'))

perimetro = 2 * m.pi * raio
area = m.pi * raio**2


print(perimetro)
print(area)

