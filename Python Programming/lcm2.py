print("Enter two number to calculate LCM")
a=int(input("Enter 1 N"))
b=int(input("Enter 2 N"))

for m in range(1, a *b +1):
    if m%a == 0 and m%b == 0:
        print("LCM of number is ", m)
        break
