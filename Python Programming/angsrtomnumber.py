def ang(n):
    
     p=0
     o=n
     while n>0:
        p=p+(n%10)*(n%10)*(n%10)
    
        n=n//10

     if  o==p:
       return True
     else:
         return False
n=int(input("n1"))

for i in range (1,n+1):
     if ang(i):
         print(i)
   
