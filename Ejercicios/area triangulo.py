#función que calcula el área de un triángulo

def area_triang(base,altura):
    area=(base*altura)/2
    return area

def main():
    base = float(input("Base:"))
    altura= float(input("Altura:"))
    area_tr=area_triang(base,altura)
    print(area_tr)

main( )
