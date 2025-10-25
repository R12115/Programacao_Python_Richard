import os
os.system("cls")

"""
Entrar com o lado de um quadrado e imprimir:
perimetro:
area:
diagonal:
"""

lado = float(input('Digite o lado: '))

perimetro = 4 * lado
area = lado * lado
diagonal = (lado**2) + (lado**2)

print(f'Perímetro: {perimetro} \nÁrea: {area} \nDiagonal: {diagonal}')
