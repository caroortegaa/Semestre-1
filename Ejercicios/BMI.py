peso=float(input())
altura=float(input())
indice=peso/altura**2
if indice<20:
    print("PESO BAJO")
elif 20<=indice<25:	
    print("NORMAL")
elif 25<=indice<30:	
    print("SOBRE PESO")
elif 30<=indice<40:
    print("OBESIDAD")
elif 40<=indice:
    print("OBESIDAD MORBIDA")
