'''
#act 25
cad=input("Escribe la cadena:")
cadenaInvertida=cad[::-1] #inicio:fin:paso
print(cadenaInvertida)
'''

'''     
escritor='hola'
cadenaInvertida=escritor[::-1]
print(cadenaInvertida)
'''
'''
palabra=input("palabra:")
def holain(palabra):
    for i in range (1,len(palabra)+1):
        print(palabra[-i],end="")

holain(palabra)
'''
#el programa quita los espcios
textot=input("palabra:")
def texto(textot):
    for i in textot:
        if i != " ":
            print(i,end="")
texto(textot)
