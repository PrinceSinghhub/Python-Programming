n = [1,2,3,4,5,50,60]
def Iteration(i):
    if i==len(n):
        pass
    else:
        print(n[i])
        Iteration(i+1)
i = 0
Iteration(i)



