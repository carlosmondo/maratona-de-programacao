# -*- coding: utf-8 -*-
def imprime_nota(qtd, cedula):
    return print("{0} nota(s) de R$ {1},00".format(qtd, cedula))
    

r=int(input())
print(r)
imprime_nota(r//100, 100)
r=r%100
imprime_nota(r//50, 50)
r=r%50
imprime_nota(r//20, 20)
r=r%20
imprime_nota(r//10, 10)
r=r%10
imprime_nota(r//5,5)
r=r%5
imprime_nota(r//2,2)
r=r%2
imprime_nota(r//1,1)
