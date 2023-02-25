n=int(input("enter the number"))
p=0
x=n
while n>0:
   p=p*10+n%10
   n=n//10
if x==p:
    print("true")
else:
    print("false")
    
    
