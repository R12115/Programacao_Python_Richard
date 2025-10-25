import os
os.system('cls')
import math as m

"""
Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante,
co-secante e co-tangente deste ângulo.
"""

angulo = int(input("Digite o Primeiro Número: "))
radiano = m.radians(angulo)
seno = m.sin(radiano)
cosseno = m.cos(radiano)


