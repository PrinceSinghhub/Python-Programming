n=input("enter the string")
p="0"
s=0
for i in n:
    if i.isdigit()==True:
        p+=i
    else:
        s+=int(p)
        p="0"
print(s+int(p))
        
