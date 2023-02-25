def fact(f):
    if f==1:
        return f
    else:
        return f * fact(f-1)

n=int(input("n"))
a=fact(n)
print(a)