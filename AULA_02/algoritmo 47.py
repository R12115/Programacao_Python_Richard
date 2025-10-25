import os
os.system('cls')

"""
Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de
ser impresso.
"""

informacao = input("Digite a informação: ")

inverso = str(reversed(informacao))

print(inverso)