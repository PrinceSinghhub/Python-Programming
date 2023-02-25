i=1
sum=0
n=int(input("ENter the number"))
while i<n:
    if (n%i==0):
        sum=sum+i
    i+=1
if sum==n:
    print(i,"is a perfect number")
else:
    print(i,"not perfect number")
    #call k

    

