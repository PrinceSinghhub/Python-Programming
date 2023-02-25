from fractions import gcd
n1=int(input("Enter a Number 1"))
n2=int(input("Enter a Number 2"))

if gcd (n1,n2) ==1:
    print("number is a co prime")
else:
    print("Number is not a co prime")