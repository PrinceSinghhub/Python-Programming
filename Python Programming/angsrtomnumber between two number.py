for i in range (1,100):
    n=i
    r=0
    a=len(str(i))
   
    while i!=0:
        c=i%10
        r=r+c**a
    
        i=i//10
    if n==r:
        print(n)
    