def potencia(n,o):
    pot=1
    for i in range(1,o+1):
        pot=pot*n
    return pot
    

def factorial(n):
    multiplicador=n
    xd=1
    for i in range(1,n+1):
        xd*=multiplicador
        multiplicador-=1
    return xd


print (potencia(2,3))
