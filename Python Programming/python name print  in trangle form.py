n=input("String")
l=len(n)
for i in range (l):
    
    for j in range (i+1):
        print(n[j],end=" ")
    print()  