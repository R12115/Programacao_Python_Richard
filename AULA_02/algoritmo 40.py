import os
os.system('cls')

"""
Entrar com dois números inteiros e imprimir a seguinte saída:
dividendo
divisor:
quociente:
resto:
"""
numero01 = int(input("Digite o Primeiro Número: "))
numero02 = int(input("Digite o Segundo Número: "))

dividendo = numero01
divisor = numero02
quociente = numero01 / numero02
resto = numero01 % numero02


print(dividendo)
print(divisor)
print(quociente)
print(resto)