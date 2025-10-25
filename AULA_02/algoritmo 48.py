"""
Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.

Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de
quilowatts gasta por uma residência e calcule. Imprima:
O valor em reais de cada quilowatt
O valor em reais a ser pago
O novo valor a ser pago por essa residência com um desconto de 10%.
"""

import os
os.system('cls')

Aliquota_desconto = 0.1

consumo = float(input('Digite o consumo da residencia (Kw): '))
salario_minimo = 1518
vlr100_kw = salario_minimo / 7
vlrKw = (salario_minimo / 7) / 100
vlr_conta = consumo * vlrKw
desconto = vlr_conta - (vlr_conta*Aliquota_desconto)

print(f'Custo por Kw: R$ {round(vlrKw,2)} \nValor total: R$ {round(vlr_conta,2)} \nValor com desconto: R$ {round(desconto,2)}')


