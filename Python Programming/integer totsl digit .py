n=int(input("enter the number"))
a=0
while n>0:
    d=n%10
    a+=d
    n=n//10
print(a)
