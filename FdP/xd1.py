def FACT(K):
    if(K==1):
        return 1
    else:
        return K*FACT(K-1)
    
def Pot(N,E):
    if(E==0):
        return 1
    else:
        return N*Pot(N, E-1)

def NroDig(F):
    if(F==0):
        return 0
    else:
        return 1 + NroDig(F//10)
    
def Inv(u):
    inv=0
    if(u==0):
        return inv
    else:
        inv= inv*10+u%10
        return Inv(u//10)
    

K=5
N=5
E=3
F=12345
u=123

print(FACT(K))
print(Pot(N,E))
print(NroDig(F))
print(Inv(u))
