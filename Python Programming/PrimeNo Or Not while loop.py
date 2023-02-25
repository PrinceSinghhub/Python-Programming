n=int(input("Enter your No ="))
b=0
a=2
if(n>2):
    while(n>a):
        if(n%a==0):
            b+=1
            break
        a+=1
    if(b==0):
      print("No is a prime no")
    elif(b==1):
      print("No is not a prime no")
elif(n<2):
    print("Please enter a valid no")



