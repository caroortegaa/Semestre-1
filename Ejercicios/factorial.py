i=1
while(i==1):
    fac=1
    num=int(input("Número: "))
    while (num>0):
        fac=fac*num
        num=num-1
    print(fac)
    i=int(input("1-Pon 1 para ingresar otro número :  2-Para salir pon 2 : "))