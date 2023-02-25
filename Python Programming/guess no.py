n=int(input("Enter your number"))
n1=int(input("Enter your adding number in n"))
n2=n+n1
n3=int(input("Enter your multiplyer in n2"))
n4=n2*n3
n5=int(input("Enter your addition number in n4"))
n6=n4+n5
n7=int(input("Enter your multipler in n6"))
n8=n6*n7
print(n8)
a=n1*n3
a1=a+n5
a2=a1*n7
print(a2)
b=n8-a2
if n>0:
    d=b%n==0
    b=1
    print(b*n)
if n==0:
    c=n8-a2
    print(c)
if n<0:
    d=b%n==0
    b=1
    print(b*n)