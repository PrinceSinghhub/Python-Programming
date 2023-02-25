a=int(input("Enter your number"))
r=0
while a>0:
    c=a%10
    r=r*10+c
    a=a//10
    print(r)

a=int(input("Enter your number"))
r=0
for i in range (1,a):

    if a>0:
        c=a%10
        r=r*10+c
        a=a//10
        print(r)

def pr(a):
    r=0
    for i in range (1,a):
        if a>0:
            c=a%10
            r=r*10+c
            a=a//10
            print(r)
a=int(input("Enter your number"))
pr(a)



