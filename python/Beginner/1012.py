# -*- coding: utf-8 -*-

numero = input().split()
a = float(numero[0])
b = float(numero[1])
c = float(numero[2])

tri = 0.5 * a * c
cir = 3.14159 * (c**2)
tra = 0.5 * (a + b) * c
qua = b ** 2
ret = a * b

print("TRIANGULO: {:.3f}\n"
      "CIRCULO: {:.3f}\n"
      "TRAPEZIO: {:.3f}\n"
      "QUADRADO: {:.3f}\n"
      "RETANGULO: {:.3f}".format(tri, cir, tra, qua, ret))
