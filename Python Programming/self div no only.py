n1=int(input("Enter a number1"))
n2=int(input("Enter a number2"))
for i in range (n1,n2):
    if i>1:
       for a in range (2, i):
           if i%a==0:
              break
       else:
           print(i)

