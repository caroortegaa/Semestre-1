#calcular el área y volumen de una esfera

import math
r= float(input("Radio: "))

area = 4 * math.pi * r**2
volumen = 4 * math.pi* r**3 / 3

print ("El área de la esfera es : " , area)
print("El volumen de la esfera es :" , volumen)
