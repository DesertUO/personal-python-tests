#suma de dos numeros 
numero1=int(input("numero 1: "))
numero2=int(input("numero 2: "))
numero3= numero1 + numero2
print(numero3)
#distancia de dos puntos 
punt1x=float(input("punto1x: "))
punt1y=float(input("punto1y: "))
punt2x=float(input("punto2x: "))
punt2y=float(input("punto2y: "))
distan= (punt2x - punt1x)**2 + (punt2y - punt1y)**2
distan=(distan)**0.5
print(distan)

#area de un triangulo
base=float(input("base: "))
altura=float(input("altura: "))
lad1=float(input("lado 1: "))
lad2=float(input("lado 2: "))
lad3=float(input("lado 3: "))
area=(base*altura)/2
perimetro=lad1 + lad2 + lad3
print("el area es: ",area)
print("el perimetro es: ",perimetro)

#area de un triangulo
a=float(input("lado 1: "))
b=float(input("lado 2: "))
c=float(input("lado 3: "))
s=(a + b +c)/2
area= (s*(s - a)*(s - b)*(s - c))**0.5
print("el area es: ", area)

lT=[]
for i in range(0,4):
    print("punto", i)
    punt1x=float(input("punto1x: "))
    punt1y=float(input("punto1y: "))
    punt2x=float(input("punto2x: "))
    punt2y=float(input("punto2y: "))
    distan= (punt2x - punt1x)**2 + (punt2y - punt1y)**2
    distan=(distan)**0.5
    lT.append(distan)
s=(lT[0] + lT[1] +lT[2])/2
area= (s*(s - lT[0])*(s - lT[1])*(s - lT[2]))**0.5
print("el area es: ", area)