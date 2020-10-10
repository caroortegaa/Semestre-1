#Leer 5 números pares e impares
#contar pares e impares
'''
#con while
contpares=0
contimpares=0
i=1
while i<=5:
    num=int(input("Número:"))
    if num%2==0:
        contpares+=1
    else:
        contimpares+=1
    i+=1
print("Pares:",contpares)
print("Impares:",contimpares)
'''
'''
contpares=0
contimpares=0
for i in range (1,6):
    num=int(input("Número:"))
    if num%2==0:
        contpares+=1
    else:
        contimpares+=1
print("Pares:",contpares)
print("Impares:",contimpares)
'''

#lea la edad de 10 personas y cuente cuantos son mayores de edad y cuantos menores de edad
'''
contmenor=0
contmayor=0
i=0
while i < 10 :
    edad=int(input("Ingresar edad:"))
    if edad<18:
        contmenor+=1
    else:
        contmayor+=1
    i+=1
print("Menor de edad:",contmenor)
print("Mayor de edad:",contmayor)
'''

#función que calcula el imc
#imc=peso/((altura)**2)
'''
def masa (peso , estatura):
    imc=peso/(pow(altura,2))
    return imc

peso=float(input("peso:"))
altura=float(input("altura:"))
indice=masa(peso,altura)
print(indice)
'''

