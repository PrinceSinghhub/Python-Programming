n=int(input("enter the number"))
count=0
x=n
while n>0:
    count=count*10+n%10
    n=n//10
print(count)
if count==x:
    print("palindrom number")
else:
    print("not palindrom number")
