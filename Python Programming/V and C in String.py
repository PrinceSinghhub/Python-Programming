s = input("Enter a String")
vowel=0
cons=0
space=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1
    elif(i==" "):
        space=space+1
    else:
        cons=cons+1

print("vowel is",vowel)
print("cons is",cons)
print("space is",space)