n=int(input("Enter a number"))
r=0
for i in range (n):
    print(i)
    if  n>0:
        
        d = n % 10
        r = r + d
        n = n // 10
print(r)
'''12
o
,1,2,3,4,5,6,7,8,9,10,11'''