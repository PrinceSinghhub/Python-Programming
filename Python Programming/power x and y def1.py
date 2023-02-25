def power(r,n2):
    for i in range (1,n2):
        r=r*n1
    return r
n1=int(input("Enter a Base"))
n2=int(input("Enter a Power"))
print(power(n1,n2))