print("count=0 one song on one time\n count>0 one song repeat infinity")
n=int(input("enter the number"))
count=int(input("enter the number"))
if count==0:
   while n>count:
      count+=1
      print(count)
else:
    while n>0:
       count+=1
       print(count,"repeat song again")
