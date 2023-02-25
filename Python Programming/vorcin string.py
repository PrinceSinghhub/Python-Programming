n = input("Enter a String")
vowel = 0
cons = 0
for i in range(0,len(n)):
    if(n[i]!=" "):
        if(n[i]=='a'or n[i]=='e'or n[i]=='i'or n[i]=='o'or n[i]=='u'or 
           n[i]=='A'or n[i]=='E'or n[i]=='I'or n[i]=='O'or n[i]=='U'):
            vowel=vowel+1
        
        else:
            cons=cons+1
print("Total Vowels=",vowel)
print("Total Cons=",cons) 

        
    
         