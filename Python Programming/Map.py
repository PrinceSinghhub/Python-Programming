a,b,c,d,e=map(int,input("enter a numbe\n").split(","))
x=(a+b+c+d+e)/5
print("% obtained =",x)
if x<=50:
    print("Passe By C Grade")
elif x>=60 and x<=90:
    print("Pass By A Grade")
elif x>=90:
    print("Pass By A+ Grade")
