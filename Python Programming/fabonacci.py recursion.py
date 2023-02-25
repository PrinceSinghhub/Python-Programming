def fabonacci(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return(fabonacci(n-1)+fabonacci(n-2))
n=int(input("enter the n"))
for i in range(n):
   print(fabonacci(i))
