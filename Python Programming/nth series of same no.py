n=int(input("Enter a number"))
n1=int(input("Enter a number"))
n2=int(input("What we want series"))
s=0
for i in range (0,n):
    print(n1,end="+")
    s+=n1
    n1=(n1*10)+n2
print("\nSum of the series is =",s)