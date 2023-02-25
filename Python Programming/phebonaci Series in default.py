def pr():
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a
        a=b
        b=b+c
n=int(input("Enter a N"))
pr()