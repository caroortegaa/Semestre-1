#programa con funciones que resuelve ecuación 2 grado f.g.

import math

def discriminante (a,b,c,):
    dis=pow(b,2)-(4*a*c)
    return dis

def raices (a,b,dis):
    x1=(-b-math.sqrt(dis))/(2*a)
    x2=(-b+math.sqrt(dis))/(2*a)
    print(x1, x2)
    

def main():
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    dis=discriminante (a,b,c)
    if dis>=0:
        print("Las raíces son iguales")
        raices(a,b,dis)
    elif dis<0:
        print("Las raíces son imaginarias")
        raices(a,b,dis)
    else:
        raices(a,b,dis)
        print(r)
    
main()
