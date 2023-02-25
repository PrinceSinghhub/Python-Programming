i = 100;
while(i<200):
    j = 2
    while(j <= (i/j)):
        if not(i%j):
            break
        j = j+1
    if (j>i/j) :
        print(i, "is prime")
    i = i+1
print("Good bye!")