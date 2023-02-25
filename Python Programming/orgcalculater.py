def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def multiply(x,y):
    return x*y
def devide (x,y):
    return x/y
def moduls (x,y):
    return x%y
def power (x,y):
    return pow(x**y)
print("Selecta a operation")
a = ("1.add")
b = ("2.sub")
c = ("3.multiply")
d = ("4.devide")
e = ("5.moduls")
f = ("6.power")
n = input("Select command a,b,c,d,e,f:")
n1 = int(input("Enter a First  Number"))
n2 = int(input("Enter a second Number"))
if n == 'a':
    print(n1+n2)
elif n == 'b':
    print(n1-n2)
elif n == 'c':
    print(n1*n2)
elif n == 'd':
    print(n1/n2)
elif n == 'e':
    print(n1%n2)
elif n == '':
    print(n1**n2)
else:
    print("Invalid input")
