def pr(n):
    
        
        if n==1:
          return 0
        if n==2:
           return 1
        else:
          return (pr(n-1)+pr(n-2))
n=int(input("N"))
for i in range (1,n+1):
  print(pr(i))