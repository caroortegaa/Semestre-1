#las listas nos permiten almacenar cualquier tipo de valor como enteros , cadenas o funciones
#si no quieres imprimir cada elemento puedes usar for
#append() agrega elementos al final de la lista
#extend() permite agregar elementos pero agrega cada elemento como un elemento más de la otra lista , a las cadenas de caracterres también las separa
#index() devuelve el número de índice del elemento que le pidas que te dé esa información
#reverse() invierte los elementos de la lista
#insert() inserta elementos a la lista
#sort() lo acomoda de menor a mayor
#lista.pop() quita algo de la lista con la posición que le pongas

#lista de n elementos enteros positivos
#forma 1
'''
lista=[ ]
mayor=0
n=int(input("Cuantos elementos:"))

for i in range (n):
    e=int(input("Elemento:"))
    lista+=[e]
    
print(lista)
'''
#forma 2
'''
n=int(input("Cuantos elementos:"))
lista=[0]*n
for i in range (n):
    e=int(input("Elemento:"))
    lista[i]=e
print (lista)
'''
#forma 3
'''
n=int(input("Cuantos elementos:"))
lista=[ ]
for i in range (n):
    e=int(input("Elemento:"))
    lista.append(e)
print (lista)
'''
#determina el elemento mayor de una lista sin funciones agregadas
'''
lista=[ ]
mayor=0
n=int(input("Cuantos elementos:"))
for i in range (n):
    e=int(input("Elemento:"))
    lista+=[e]
    if lista [i]>mayor:
        mayor=lista[i]
print(lista)
print("El mayor de la lista es :",mayor)
'''
#ordenar una lista
'''
n=int(input("Cuantos elementos:"))
lista=[0]*n
for i in range (n):
    e=int(input("Elemento:"))
    lista[i]=e
print(lista)
lista.sort()
print(lista)
'''
#random es una librería
#randint() genera num aleatorios entre el rango que le pongas
#uniform() genera numeros decimales entre un valor y otro

#generar una lista aleatoria
'''
import random
lista=[]

for i in range (0,7):
    lista.append(random.randint(0,9))
    
print(lista)
'''
#generar una lista aleatoria (con shuffle) y revolver los elementos
'''
import random
lista=[]
for i in range (0,7):
    lista.append(random.randint(0,9))
print(lista)
random.shuffle(lista)
print(lista)
'''
#hacer un tablero
'''
lista=[["_","1","2","3"],
       ["_","_","_","_"],
       ["2","_","_","_"]]
def imprimir (lista):
    for i in lista :
        for j in i:
            print(j,end=" ")
        print()
imprimir(lista)
'''
'''
#Realizar un programa que contenga una lista con 10 valores enteros.
#Informar de cuántos de ellos son superiores a 100. Los valores son:
#lista=[213,44,578,123,100,56,78,1000,2345,1278]

lista=[213 , 44 , 578 , 123 , 100 , 56 , 78 , 1000 , 2345 , 1278]

print("Los números mayores a 100 son: ")

for numero in lista:
    if numero > 100:
        print(numero)
'''

#Una empresa divide el trabajo en dos turnos (mañana y tarde) en las que trabajan 6 empleados (3/turno).
#Agrupar los sueldos de los empleados en dos listas y mostrar después las listas por consola.
'''
lista_manana = []
lista_tarde = []

manana = 3
tarde = 3

print("TURNO DE LA MAÑANA")
for valor in range(manana):
    nombre = input("Ingresa el nombre del empleado: ")
    lista_manana.append(nombre.capitalize())
    sueldo = input(f"Ingresa el sueldo de {nombre.capitalize()}: ")
    lista_manana.append(sueldo)

print("TURNO DE LA TARDE")
for valor in range(tarde):
    nombre = input("Ingresa el nombre del empleado: ")
    lista_tarde.append(nombre.capitalize())
    sueldo = input(f"Ingresa el sueldo de {nombre.capitalize()}: ")
    lista_tarde.append(sueldo)

print("La información de los empleados del turno de la mañana es la siguiente: ")
print(lista_manana)
print("La información de los empleados del turno de la tarde es la siguiente: ")
print(lista_tarde)
'''

#Realizar un programa que permita crear una lista y almacenar los nombres de n países.
#Ordenar alfabéticamente la lista e imprimirla.
'''
lista = []

cant = int(input("¿Cuántos nombres de países deseas almacenar?: "))
while cant <= 0:
    cant = int(input("Por favor ingresa un número positivo, ¿Cuántos nombres de países deseas almacenar?: "))
for num in range(cant):
    pais = str(input("Ingresa el nombre del país: "))
    lista.append(pais.capitalize())

print("La lista de países en orden alfabético es la siguiente: ")
print(sorted(lista))
'''

#Realizar un programa que permita cargar una lista de n elementos enteros. Ordenarla de mayor a menor
#e imprimir los resultados obtenidos. Informar también del número mayor y del número menor.
'''
lista = []

cant = int(input("¿Cuántos números enteros deseas almacenar?: "))
while cant <= 0:
    cant = int(input("Por favor ingresa un número positivo: "))
for num in range(cant):
    numero = int(input("Ingresa el número entero: "))
    lista.append(numero)
    
print("Los resultados obtenidos son los siguientes: ")
print(sorted(lista))
print(f"El número mayor fue {max(lista)}, y el menor fue {min(lista)}")
'''

#Realizar un programa que permita cargar n países y la cantidad de habitantes que residen en cada uno.
#Imprimir cada país con su número de habitantes correspondiente.
'''
lista = []

cant = int(input("¿Cuántos países deseas introducir?: "))
while cant <= 0:
    cant = int(input("Por favor ingresa un valor positivo: "))
for num in range(cant):
    pais = input("Ingresa el nombre del país: ")
    habitantes = input("Ingresa el número de habitantes (en millones): ")
    lista.append(pais.capitalize())
    lista.append(habitantes)
    
print(lista)
'''

#Realizar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un entero,
#el segundo es una lista con dos enteros, etc. La lista debería tener la siguiente estructura
#[[1], [1, 2], [1, 2, 3], ...]
'''
lista = []
cant = 50
valor = 1

for a in range(cant):
    lista.append([])
    num = 1
    for b in range(valor):
        lista[a].append(num)
        num += 1
    valor += 1
print(lista)
'''
#Crear una lista por asignación con la cantidad de elementos y niveles de lista que desee.
#Después imprimir el resultado de la lista principal.
'''
lista = []

cant = int(input("¿Cuántos elementos deseas almacenar?: "))
while cant <= 0:
    cant = int(input("Por favor ingresa un número positivo: "))
for num in range(cant):
    elemento = input("Ingresa el elemento: ")
    lista.append(elemento)
    
print(lista)
'''
#Una matriz es una lista de listas

#Determinar la mayor y la menor temp , promedio , ordenar de menor a mayor

'''
Lista_temp=[5.5,12.48,31.54,20.45,17.7,28.3,35.4]
mayor=0
menor=0
for i in range (len(Lista_temp)):
    a=sorted(Lista_temp)
    suma=sum(Lista_temp)
    prom=suma/len(Lista_temp)
    if Lista_temp[i]>mayor:
        mayor=Lista_temp[i]
for d in range (len(Lista_temp)):
    if Lista_temp[d]<menor:
        menor=Lista_temp[d]
        
print("el número mayor es :",mayor)
print("el número menor es :",menor)
print (Lista_temp)
print(a)
print("el promedio es :",prom)
'''

#Matriz
'''
suma=0
su=0
s=0
matriz= [[0,2,4],
         [1,3,5],
         [7,8,9]]
for i in range (len(matriz)):
    for j in range (len(matriz)):
        if i==j:
            suma=suma+matriz[i][j]
        if i<j:
            su=su+matriz[i][j]
        if i>j:
            s=s+matriz[i][j]
            
print(suma)
print(su)
print(s)
'''
'''
cad='Hola la casa está muy lejos'
subcad=str(input())
'''
'''
#Programa que genera una matriz y la dibuja

def dibujaMatriz(A):
    for columna in range(len(A)):
        print("[", end=" ")
        for renglon in range(len(A[columna])):
            print("{:<7s}".format(str(A[columna][renglon])), end=" ")
            
        print("]")
        
matriz = [[1,2,3],[200,4,87],[200000,50,4]]
dibujaMatriz(matriz)
'''
'''
#Matriz aleatoria de 5x3

from random import randint

def dibujaMatriz(A):
    for columna in range(len(A)):
        print("[", end=" ")
        for renglon in range(len(A[columna])):
            print("{:<7s}".format(str(A[columna][renglon])), end=" ")
            
        print("]")
        
matriz = [[1,2,3],[200,4,87],[200000,50,4]]
dibujaMatriz(matriz)


#columnas = 2
#renglones = 3
#matriz1 = []
#
#for i in range(renglones):
#    renglon = [0]*columnas
#    matriz1.append(renglon)
#    
#dibujaMatriz(matriz1)

from random import randint
columnas = 5
renglones = 3
matriz2 = []

for i in range(renglones):
    matriz2.append([])
    for j in range(columnas):
        dato = randint(1,100)
        matriz2[i].append(dato)
    
dibujaMatriz(matriz2)
'''
'''
#juego de memoria
import random
import sys

x=0
y=0
x2=0
y2=0
p1 = 0
p2 = 0
matrixclosed = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]
matrixopened = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
raiz = 1

def memorama():
    imprimir()
    print('Jugador 1')

    x = int(input('Ingresa x de tu primer carta: '))
    if x > 5:
        print('ERROR')
        memorama()

    y = int(input('Ingresa y de tu primer carta: '))
    if y > 5:
        print('ERROR')
        memorama()

    matrixclosed[x][y] = matrixopened[x][y]

    imprimir()

    x2 = int(input('Ingresa x de tu segunda carta: '))
    if x2 > 5:
        print('ERROR')
        matrixclosed[x][y] = '-'
        memorama()
    else:
        y2 = int(input('Ingresa y de tu segunda carta: '))
        if y2 > 5:
            print('ERROR')
            matrixclosed[x][y] = '-'
            memorama()

    matrixclosed[x2][y2] = matrixopened[x2][y2]

    condiciones(x,y,x2,y2)

    imprimir()

def memorama2():
    imprimir()
    print('Jugador 2')

    x = int(input('Ingresa un valor en la horizontal: '))
    if x > 5:
        print('ERROR')
        memorama2()

    y = int(input('Ingresa un valor en la vertical: '))
    if y > 5:
        print('ERROR')
        memorama2()

    matrixclosed[x][y] = matrixopened[x][y]

    imprimir()

    x2 = int(input('Ingresa un valor en la horizontal: '))
    if x2 > 5:
        print('ERROR')
        matrixclosed[x][y] = '-'
        memorama2()
    else:
        y2 = int(input('Ingresa un valor en la vertical: '))
        if y2 > 5:
            print('ERROR')
            matrixclosed[x][y] = '-'
            memorama2()

    matrixclosed[x2][y2] = matrixopened[x2][y2]

    condiciones2(x,y,x2,y2)

    imprimir()

def condiciones(x,y,x2,y2):
    global p1
    if matrixclosed[x][y] != matrixclosed[x2][y2]:
        matrixclosed[x2][y2] = "-"
        matrixclosed[x][y] = "-"
        respuesta = str(input('¿Quiere seguir jugando? si/no: '))
        if respuesta == 'si':
            memorama2()
        elif respuesta == 'no':
            print('El jugador tiene',p1,'pares')
            print('El jugador tiene',p2,'pares')
            if p1 > p2:
                print('El ganador fue el jugador 1')
            elif p2 > p1:
                print('El ganador fue el jugador 2')
            elif p2 == p1:
                print('Fue un empate!')
            elif p1 == p2:
                print('Fue un empate!')
            sys.exit()    
    else:
        p1 += 1 
        memorama()

def condiciones2(x,y,x2,y2):
    global p2
    if matrixclosed[x][y] != matrixclosed[x2][y2]:
        matrixclosed[x2][y2] = "-"
        matrixclosed[x][y] = "-"
        respuesta = str(input('¿Quiere seguir jugando? si/no: '))
        if respuesta == 'si':
            memorama()

        elif respuesta == 'no':
            print(p1)
            print(p2)
            if p1 > p2:
                print('El jugador tiene',p1,'pares')
            elif p2 > p1:
                print('El jugador tiene',p2,'pares')
            elif p2 == p1:
                print('Fue un empate!')
            elif p1 == p2:
                print('Fue un empate!')
            sys.exit()
    else:
        p2 += 1
        memorama2()

def imprimir():
    contador = 0
    print('  0 1 2 3 4 5 \n')

    for i in range(6):
        print(contador, '', end = '')
        contador += 1
        for j in range(6):
            print((matrixclosed[i][j]),'', end = '')

        print('\n')

def main():
    while raiz == 1:
        random.shuffle(matrixopened)
        for i in matrixopened:
            random.shuffle(i)
        memorama()

main()
'''




        


