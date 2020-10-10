#programa que lea 10 números solicitados y calcule la raíz cuad. de cada número
#lo eleve al cubo cada raíz, y sumarle la potencia 3
#imprimir suma
import math

num = []

for i in range(10):
    num.append(int(input()))
#append agrega elementos al final de una lista
    r= math.sqrt(num[i])
    cubo=r**3
    suma=r+cubo
    print(suma)
    num[i] = suma
sumaTotal = sum(num)
print(sumaTotal)
    


