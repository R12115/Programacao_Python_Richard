"""
Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
peri metro
area
diagonal:
"""

import os
os.system('cls')
import math as m

base = int(input('Digite o valor da base: '))
altura = int(input('Digite o valor da altura: ')) 

perimetro = 2 *(base + altura)
area = base * altura
diagonal = m.pow(base,2) + m.pow(altura,2)


print(f'Perímetro: {perimetro} \nÁrea: {area} \nDiagonal: {diagonal}')