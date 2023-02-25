n=input("Enter a String")
temp=""
sum1=0
for i in n:
    if i.isdigit():
        temp+=i
    else:
        sum1+=int(temp)
        temp = "0"
a=sum1+int(temp)
print(a)



        