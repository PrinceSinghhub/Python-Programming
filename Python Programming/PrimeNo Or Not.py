n=int(input("Enter your No ="))
a=0
if(n>2):
    for i in range(2,n):
        if (n % i == 0):
            a += 1
            break
elif(n<2):
    print("Please enter a valid no")
if(a==0):
    print("No is a prime no")
elif(a==1):
    print("No is not a prime no")





