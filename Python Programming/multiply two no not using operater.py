a=int(input("Enter n Number"))
b=int(input("Enter n Number"))
if a>0 and b>0:
    c = 0
    for i in range(1, b + 1):
        c += a
    print(c)
if b<0 and a>0:
    z=-(b)
    #print(z)
    c = 0
    for i in range(1,z+1):
        c+=a
    print(-c)
if a<0 and b<0:
    c=-(a)
    d=-(b)
    e=0
    for j in range (1,d+1):
        e=e+c
    print(e)
if a<0 and b>0:
    c=-(a)
    d=b
    f=0
    for i in range (1,d+1):
        f+=c
    print(-f)
if a==0 and b==0:
    print(0)
if a>0 and b==0:
    print(0)
if a==0 and b>0:
    print(0)
if a <0 and b==0:
    print(0)
if b<0 and a==0:
    print(0)

