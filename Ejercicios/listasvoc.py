'''
lista=[3,4,5]
lista2=[6,7,8]
lista3=[]
for x in range (0,len(lista)):
    x1=lista[x]
    x2=lista2[x]
    lista3.append(x1+x2)
print(lista3)
'''
'''
n=0
n1=0
n2=0
n3=0
lista=[]
lista2=[]
lista3=[]
n=int(input()) 
n1=int(input())
print('/')
n2=int(input()) 
n3=int(input())
print('*')
def sumar():
    suma=sum(x1+x2)
    return suma
def su():
    su=sum(x3+x4)
    return su

for x in range (0,len(lista)):
    x1=lista[n]
    x2=lista[n1]
    sumar()
    lista3.append(suma)
for x in range (0,len(lista2)):
    x3=lista[n2]
    x4=lista[n3]
    su()
    lista3.append(su)
print(lista3)
'''
'''
lista=[ ]
palabra=input()
palabra=lista.append(palabra)
for a in range (len(palabra,1,-1)):
    a=lista.reverse(palabra)
    print(a)
    
    if a==palabra :
        print ("Es un palindromo")
    else:
        a!=palabra
    print("No es un palindromo")
'''
'''
palabra=str(input())
pali=palabra[::-1]
if palabra==pali:
    print("Es un palindromo")
else:
       print("No es un palindromo")
       '''
'''
str = "Computacion"
print(str[5 : ])
str = "Computacion"
print(str[ : 5])
'''
'''
n=int(input("Cuantos elementos:"))
lista=[ ]
for i in range (n):
    e=int(input("Elemento:"))
    lista.append(e)
print (lista)

'''



