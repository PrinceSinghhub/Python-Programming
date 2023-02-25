def pr(s,n):
    if n==0:
        print(s[0])
    else:
        print(s[n],end="")
        pr(s,n-1)
s=input("Enter your string")
pr(s,len(s)-1)
