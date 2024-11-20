import NumeroFunciones as NP
import ModulosPrim as MP

def main():
    MP.MostrarAsterisks(100)
    numeroA = int(input("Ingrese un número positivo: "))
    print(NP.NumeroInvertido(numeroA))
    MP.MostrarAsterisks(100)
    print("Ahora ingrese 2 números: ")
    num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el primer número: "))
    print(NP.SumaDosNumeros(num1,num2))
    
if __name__ == "__main__":
    main()