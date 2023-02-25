a=["oop","om", "rahul","sohan"]
b=len(a)
c=0
while c<len(a):
    if a[c].startswith("o")==True:
        print("hello",a[c])
    else:
        print("hi")
        c+=1
