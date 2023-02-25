def pr(s):
    if len(s)==0:
        return True
    else:
        if s[0]==s[len(s)-1]:
            return pr(s[1:len(s)-1])
        else:
            return False
s=input("Enter Your String")
if pr(s)==True:
    print("Yes")
else:
    print("No")