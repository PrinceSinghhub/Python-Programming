n=int(input("enter the number the number"))
for i in range(1,n+1):
    a=i
    fact=1
    for j in range(1,a+1):
        fact=fact*j
    print(fact)
        