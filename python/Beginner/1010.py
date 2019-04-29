# -*- coding: utf-8 -*-
# 1010 - Simple Calculate
total = 0
for i in range(0, 2):
    produto = input().split()
    total += int(produto[1]) * float(produto[2])
    
print("VALOR A PAGAR: R$ {:.2f}".format(total))
