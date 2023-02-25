income=float(input("enter the income"))
if income<250000:
     print("not tax")
elif income>250000 and 500000<=income:
    income=income-250000
    tax=income*0.05
    print("your taxes is",tax)
elif income>500000 and income<=1000000:
    income=income-500000
    tax=income*0.20
    print("your tax is",tax)
elif income>1000000:
    income=income-1000000
    tax=income*0.30
    print("your tax is",tax)
