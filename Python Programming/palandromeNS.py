a=int(input("Entear a N"))
b=input("Entear a String")
c=str(a)
d=c[::-1]
print("Your Number is =",a)
print("Your Reversed Number is =",d)
if c==d:
    print("Number is a Palandrome")
else:
    print("Number not a Palandrome")
e=b
f=b[::-1]
print("Your String is =",b)
print("Your Reversed string is =",f)
if e==f:
    print("String is a Palandrome")
else:
    print("String not a Palandrome")