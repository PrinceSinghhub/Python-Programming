n=int(input("enter the nmuber"))
count=0
while n>0:
    d=n%10
    count+=d
    n=n//10
print(count)
