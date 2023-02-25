year = int(input("ENTER ANY YEAR:  "))

if (year % 400 == 0):
    print(year, "is a Leap Year")
elif (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a leap Year")
    
    
