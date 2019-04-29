# -*- coding: utf-8 -*-
# 1002 - Area of a Circle - Sequencial - Level 1
def return_float():
    
    return float(input())


n = 3.14159
r = return_float()
a = n * (r*r)
print("A={:.4f}".format(a))
