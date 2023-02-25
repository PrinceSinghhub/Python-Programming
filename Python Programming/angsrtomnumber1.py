n=int(input("n"))
p=0
o=n
while n>0:
   p=p+(n%10)*(n%10)*(n%10)
   n=n//10
print(p)
if  o==p:
    print("is a angstroam")
else:
    print("is not a angstroam")