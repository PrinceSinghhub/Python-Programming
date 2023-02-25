print("Selecta a operation")
n1 = int(input("Enter a First  Number"))
n = input("Select Operator")
n2 = int(input("Enter a second Number"))
if n =='+':
    print(n1+n2)

elif n == '-':
    print(n1-n2)
elif n == '*':
    print(n1*n2)
elif n == '/':
    print(n1/n2)
elif n == '%':
    print(n1%n2)
elif n == '**':
    print(n1**n2)
elif n== '**0.5':
    print(n1**0.5)
else:
    print("Invalid input")



