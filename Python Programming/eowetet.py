n=int(input("enter the number"))
for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()
