import math
def potencia(n,o):
    pot=1
    for i in range(1,o+1):
        pot=pot*n
    return pot
    

def factorial(n):
    if (n==0):
        return 1
    multiplicador=n
    xd=1
    for i in range(1,n+1):
        xd*=multiplicador
        multiplicador-=1
    return xd

A=float(input("Ingrese su angulo grados sexagesimales: "))
A=A*math.pi/180
coseno=0
signo=1
precision=10

for k in range(0,precision*2,2):
    numerador= signo * potencia(A,k)
    denominador= factorial(k)
    signo*=-1
    coseno= coseno + numerador/denominador

print(coseno)
print (math.cos(A))


