# -*- coding: utf-8 -*-
# 1035 - Selection Test 1 

i=input().split()
v = [int(j) for j in i]
a=v[1]>v[2] and v[3]>v[0]
b=(v[2]+v[3])>(v[0]+v[1])
c=v[2] > 0 and v[3] > 0
d=v[0] % 2 == 0
if (a and b and c and d):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
