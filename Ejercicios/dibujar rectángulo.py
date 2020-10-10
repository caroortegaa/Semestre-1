#Solicitar base y altura y dibujar el rectángulo
#base:4
#altura:2
#****
#****

def rectangulo(base,altura):
    for i in range (1,altura+1):
        for j in range (1,base+1):
            print("*",end="")
        print(" ")

base=int(input("Base: " ))
altura=int(input("Altura: "))
rectangulo(base,altura)

