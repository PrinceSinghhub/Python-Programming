x=int(input("Enter your number = "))
a=[]
for i in range(x):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
               break;
        else:
            a.append(i)
# print(a)
a1=0
b=1
z=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]+a[j]==x:
            z+=1
            print("the addition of",a[i],"+",a[j],"=", x)
            break
print("the total compression is = ",z)
   
    
    