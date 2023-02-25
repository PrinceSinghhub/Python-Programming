def pr(n):
    if n==1:
        return 1
    else:
        return (n*pr(n-1))
n=int(input("enter a number"))
print(pr(n))

2
