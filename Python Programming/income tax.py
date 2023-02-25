n=int(input("Enter you Money"))
tax=0
if n<=250000:
    tax=0
elif n>250000 and n<=500000:
    tax=(n-10000)*5/100
else:
    tax=0
    tax=10000*5/100
    tax += (n - 20000)*20/100
print("income tax is =",tax)

    
    
    
