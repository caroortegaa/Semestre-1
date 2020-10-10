y = [' ',' ']
z = [' ',' ']
x = [y,z]
for i in range(len(y)):
     y[i] = int(input())
for k in range(len(z)):
    z[k] = int(input())


determinante=x[0][0] * x[1][1] - x[0][1]*x[1][0]

print(determinante)


