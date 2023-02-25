def pr (s):
    a=len(s)
    for i in range (a):
        #print(i)

        if s[i] == "c":
            return s.replace("c","3")
        else:

            return pr(s[i])
s=input("enter a string")
print(pr(s))
