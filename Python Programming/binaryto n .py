n = int(input("Enter a Bineary"))

sum = 0
i = 0
while n!=0:
    rem = n%10
    sum = sum + rem * pow(2,i)
    n = int(n/10)
    i=i+1
  
    print(sum)
    
    