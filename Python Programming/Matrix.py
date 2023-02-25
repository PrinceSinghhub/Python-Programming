print("enter the matrix dimession (only valid 4 and 9 Digit)")
n=int(input("Enter a N"))
if n == 2:
    n1,n2,n3,n4=map(int,input("enter a row").split(","))
    print(n1*n4-n2*n3)
else:
    r1,r2,r3,ro1,ro2,ro3,row1,row2,row3=map(int,input("enter a row").split(","))
    n1=r1
    m1=(ro2*row3-row2*ro3)
    l=n1*m1
    n2=(-r2)
    m2=(ro1*row3-row1*ro3)
    p=n2*m2
    n3=r3
    m3=(ro1*row2-row1*ro2)
    o=n3*m3
    d=l+p+o
    print(d)

    
