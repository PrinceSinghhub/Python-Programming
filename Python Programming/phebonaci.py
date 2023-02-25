def febonaci(n):

    if n < 0:
        print("invalid input")
    elif n == 0:
        return n
    elif n == 1:
        return n
    else:
        return(febonaci(n-1)+febonaci(n-2))
n=int(input("enter the number"))
for i in range(n):
    print(febonaci(i))

