import os
os.system('cls')
import math as m

"""
Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante,
co-secante e co-tangente deste ângulo.
"""

angulo = int(input("Digite o Ângulo: "))
radiano = m.radians(angulo)
seno = m.sin(radiano)
cosseno = m.cos(radiano)
tangente = m.tan(radiano)
secante = 1 / seno
co_secante = 1 / cosseno
co_tangente = 1 / tangente

print(f'Seno: {seno} \nCosseno: {cosseno} \nTangente: {tangente} \nSecante: {secante} \nCo-secante: {co_secante} \nCo-tangente: {co_tangente}')



