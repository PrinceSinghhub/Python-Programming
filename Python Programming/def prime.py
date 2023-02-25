
def prime(n,n1):
    if  n1==1:
         print("not prime number")
    for  i in range(n,n1+1):
         if n>1:
             for j in range(2,i):
                 if i%j==0:
                  break
             else:
                  print(i)

n=int(input("enter the number"))
n1=int(input("enter the number"))
prime(n,n1)



