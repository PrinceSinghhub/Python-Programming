n=int(input("enter the number:"))
n1=0
n2=1
count=0
for i in range(1,n+1):
    if count<n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1
