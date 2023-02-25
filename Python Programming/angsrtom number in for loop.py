n=int(input("n"))
a=n
b=0
for i in range (n):
    if i>0:
        b=b+(n%10)*(n%10)*(n%10)
        n=n//10
if a==b:
    print("Yes a Angstrome number")
else:
    print("Not")
        
        