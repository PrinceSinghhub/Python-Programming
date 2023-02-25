def pr(x,y):
    if y==0:
        return 1
    else:
        return (x*pr(x,y-1))
x=int(input("Enter your base"))
y=int(input("Enter your pouer"))
z=pr(x,y)
print(z)
