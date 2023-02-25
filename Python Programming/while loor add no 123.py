n=int(input("Enter a number"))
r=0
while n>0:
    d = n % 10
    r = r + d
    n = n // 10
print(r)