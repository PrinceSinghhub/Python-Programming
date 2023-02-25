n = int(input())
f=0;s=1;t=0

while(t<n):
    print(t, end=" ")
    f=s;s=t;t=f+s

