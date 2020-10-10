#programa convertidor de monedas
print("1.Dólares : ")
print("2.Euros : ")
print("3.Libras Esterlinas : ")
op=int(input("Selecciona 1,2 o 3: "))
pesos=float(input("pesos mexicanos a convertir: "))
if op==1:
    dolares=pesos/19.92
print(pesos , "pesos equivalen a :" ,"%2.2f" % dolares , "dólares")
