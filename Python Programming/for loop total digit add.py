n=int(input("enter the number"))
count=0
for i in range(n):
 if n>0:
    d=n%10
    count+=d
    n=n//10
print(count)
