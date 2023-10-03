import math
a = str(input())
if a == 'sphere':
    r = float(input())
    reslutado = 4/3 * math.pi * r**3
elif a == 'cone':
    r = float(input())
    h = float(input())
    resultado = 1/3 * math.pi * (r**2) * h
elif a == 'cylinder':
    r = float(input())
    h = float(input())
    resultado = math.pi * (r**2) * h

resultado = round(resultado,1)
print(resultado) 
