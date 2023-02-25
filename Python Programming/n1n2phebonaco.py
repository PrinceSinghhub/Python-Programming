n1=int(input("Enter a 1 Number"))
n2=int(input("Enter a 2 Number"))
first=n1
second=n2

if n1 and n2==0:
    print("indivadual number")
else:
    for i in range (n1 , n2):
       print(first)
       temp = first
       first = second
       second = temp+second