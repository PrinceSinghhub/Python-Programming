print("Selecta a operation")
n1 = int(input("Enter a First  Number"))
import math
log=math.log(n1)
e=math.e**n1
n = input("Select Operator")
if n == '**0.5':
    print(n1**0.5)
elif n=='log':
    print(log)
elif n== 'e':
    print(e)
else:
    n2 = int(input("Enter a Second Number"))
    if n == '+':
        print(n1 + n2)
    elif n == '-':
        print(n1 - n2)
    elif n == '*':
        print(n1 * n2)
    elif n == '/':
        print(n1 / n2)
    elif n == '%':
        print(n1 % n2)
    elif n == '**':
        print(n1 ** n2)
    else:
        print("indivadual code")
