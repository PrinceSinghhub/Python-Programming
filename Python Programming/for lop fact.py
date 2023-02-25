n=int(input("Enter a Number"))
f=1
for i in range (1,n):
    f=f*n
    n-=1
    print(f)