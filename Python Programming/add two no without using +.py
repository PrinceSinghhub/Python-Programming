a=int(input("Enter a Number 1"))
b=int(input("Enter a Number 1"))
while b!=0:
    carry=a&b
    a=a^b
    b=carry << 1
print(a)
