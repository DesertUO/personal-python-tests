n=int(input("en que puesto "))
sum=0
for i in range(0,n):
    sum = sum + 2**(i-1)
    ult=2**(i-1)
sum=sum*2
print(sum)
print(ult)