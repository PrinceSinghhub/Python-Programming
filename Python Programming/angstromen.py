n=int(input("enter the number"))
count=0
while n>0:
    count=count+(n%10)*(n%10)*(n%10)
    n=n//10
print(count)
