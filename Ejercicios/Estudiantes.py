

groupA=0
groupB=0
groupC=0
groupD=0

n=int(input("ponga # estudiantes: "))
i=0
while i < n:
    alt=int(input("altura estudiantes: "))
    if alt<=150:
        groupA +=1
        print("Hay", groupA,"alumnos en grupoA")
    elif 150<alt<=165:
        groupB +=1
        print("Hay", groupB,"alumnos en grupoB")
    elif 165<alt<=180:
        groupC +=1
        print("Hay", groupC,"alumnos en grupoC")
    elif 180 < alt:
        groupD +=1
        print("Hay", groupD,"alumnos en grupoD")
    else :
        print ("invalid values")
    i+=1
