def cs(n):
    if n!=0:
        return n+cs(n-1)
    else:
        return 0
n=int(input("enter the number"))
print(cs(n))
