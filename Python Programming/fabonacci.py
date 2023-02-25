def fabonacci(n):
    if n<=1:
        return n
    else:
        return(fabonacci(n-1)+fabonacci(n-2))
num=int(input("enter the number:"))
if num<=0:
    print("please enter positive number")
else:
    for i in range(num):
        a=fabonacci(i)
        print(a)
