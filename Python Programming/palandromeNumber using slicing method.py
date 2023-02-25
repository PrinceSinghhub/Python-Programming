x=int(input("Entear a N"))
y=str(x)
z=y[::-1]
print("Your N is =",x)
print("Your Reversed N is =",z)
if y==z:
    print("yes")
else:
    print("no")