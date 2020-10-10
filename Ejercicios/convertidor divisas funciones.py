#convertidor de divisas
#1. euros
#2. dolares usa
#3. dolares canadá

def menu():
    print("1. Euros: ")
    print("2. Dólares usa: ")
    print("3. Dólares canadá: ")
    
def dolares (pesos,dolares):
    dolares=pesos/20
    return dolares
def dolarcanad (pesos,dolarcanad):
    dolarcanad=pesos/15
    return dolarcanad
def euros (pesos,euros):
    euros=pesos/22
    return euros

def main():
    pesos=float(input("Ingrese los pesos a cambiar: "))
    opcion=int(input("1. Euros 2. Dólares usa 3. Dólares canadá "))
    if opcion==1:
        dolar=dolares(pesos,dolares)
        print("Es igual a : " , dolar , "dólares (USA)")
    elif opcion==2:
        dc=dolarcanad(pesos,dolarcanad)
        print("Es igual a : " , dc , "dólares canadienses")
    elif opcion==3:
        e=euros (pesos,euros)
        print("Es igual a : " , dc , "euros")
