r=int(input("Enter no of Rows"))
c=int(input("Enter a Collum"))
matrix=[]
for i in range (r):
    a=[]
    print('i=',i)
    for j in range(c):
        print('j=',j)
        n=int(input("Enter no"))
        a.append(n)
    matrix.append(a)
    print(a)
print(matrix)
for i in range (r):
    for j in range (c):
        print(matrix[i][j],end=" ")
    print()
        
