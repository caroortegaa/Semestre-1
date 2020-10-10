#la función recibe cadena y letra 
def cambiar (cadena , letra):
    i=0
    #len=length
    while i < len(cadena):
        #el corchete indica la posición
        letra1=cadena[i]
        if letra1 != letra:
            print("*", end="")#end no hace saltos de línea y escrible lo sig al lado
        else:
            print(letra,end="")
        i+=1
        
#parte fuera de la función
cadena=input("Cadena de caracteres: ")
letra=input("Letra: ")
cambiar(cadena,letra)
