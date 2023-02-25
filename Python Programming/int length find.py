n=int(input("Enter a number"))
b=0
while n!=0:
    n//=10
    b+=1
    print(b,end=" ")