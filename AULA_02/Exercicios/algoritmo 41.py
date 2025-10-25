import os
os.system('cls')

"""
Entrar com quatro números e imprimir a média ponderada, sabendo-se que os
pesos são respectivamente: 1, 2, 3 e 4.
"""

numero01 = int(input("Digite o Primeiro Número: "))
numero02 = int(input("Digite o Segundo Número: "))
numero03 = int(input("Digite o Primeiro Número: "))
numero04 = int(input("Digite o Segundo Número: "))


media_pond = (numero01*1 + numero02*2 + numero03*3 + numero04*4) / 10

print(media_pond)