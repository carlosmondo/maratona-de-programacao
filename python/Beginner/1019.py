# -*- coding: utf-8 -*-
# 1019 - Time Conversion
T=int(input())
H=T//3600
M=(T//60)%60
S=T%60

print("{0}:{1}:{2}".format(H, M, S))
