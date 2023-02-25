n=input("enter the string")
s="0"
p=0
for i in n:
    if s.isdigit()==True:
        s+=i
    else:
        d+=int(s)
        s="0"
print(d+int(s))
        
    
