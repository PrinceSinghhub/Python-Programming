n=int(input("enter the row"))
list1=[]
for i in range(n):
    templist=[]
    for j in range(0,i+1):
        if j==0 or j==i:
            templist.append(1)
        else:
            templist.append(list1[i-1][j-1]+list1[i-1][j])
        list1.append(templist)
print(list1)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(list1[i][j],end=" ")
    print()
