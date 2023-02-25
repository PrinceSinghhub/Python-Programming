n=int(input("N1"))
p=int(input("Enter a Power"))
expon=1
for i in range(1,p+1):
    expon=expon*n
print("the result of ", n,"p",p,"is",expon)