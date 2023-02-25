from numpy import*
a=array([1,12,3,4,5])
b=array([6,7,8,9,10])
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)
x=len(a)
a1=0
b1=0
while(a1<x):
    print(a[a1]>b[b1])
    a1+=1
    b1+=1