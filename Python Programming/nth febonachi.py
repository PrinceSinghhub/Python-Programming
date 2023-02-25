n = int(input())
f=0;s=1;t=0

while(n>=0):
    print(t,end=" ")
    f = s
    s = t
    t = f + s
    n-=1
