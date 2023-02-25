n1 = int(input("Enter Starting year"))
n2= int(input("Enter Starting year"))
for i in range(n1,n2):
    if i%400==0:
        print (i)
    elif i%4 == 0 and i% 100!=0:
        print(i)