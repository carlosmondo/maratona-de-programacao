numero = input().split()
a = int(numero[0])
b = int(numero[1])
c = int(numero[2])

maiorAB = (a+b+abs(a-b))/2
maiorAC = (maiorAB+c+abs(maiorAB-c))/2

print("{:.0f} eh o maior".format(maiorAC))
