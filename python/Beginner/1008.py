# -*- coding: utf-8 -*-
# 1008 - Salary

numero = int(input())
horas = int(input())
per_hora = float(input())

print("NUMBER = {:d}\n"
      "SALARY = U$ {:.2f}".format(numero, horas*per_hora))
