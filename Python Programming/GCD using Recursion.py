def pr(p,q):
    if q==0:
        return p
    else:
        return (pr(q,p%q))
p=int(input("enter a higher number"))
q=int(input("enter a lower number"))
print(pr(p,q))