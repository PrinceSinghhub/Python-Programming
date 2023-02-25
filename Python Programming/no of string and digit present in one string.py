n=input("Enter a String")
c=0
v=0
for i in n:
    if i.isalpha():
        c+=1
    elif i.isdigit():
        v+=1
print("Total N of String is =",c)
print("Total N in String is =",v)
    