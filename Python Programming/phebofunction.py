def febonaci(n):
    first=0
    second=1

    if n<0:
       print("invalid input")
    elif n==0:
       return first
    elif n==1:
       return second
    else:

        for i in range(n):


        
          print(first)
          temp = first
          first = second
          second = temp+second

        return second
n=int(input("Enter a number"))
febonaci(n)  
