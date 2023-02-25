n=int(input("enter the number"))
n1=int(input("enter the number"))
for i in range(n,n1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

