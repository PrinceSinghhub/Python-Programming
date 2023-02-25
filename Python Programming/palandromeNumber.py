n=int(input("e t n"))
p=0
o=n
while n>0:
    p=p*10+n%10
    n=n//10
print(p)
if  o==p:
   print("palindrome n")
else:
   print("not palindrome n")
