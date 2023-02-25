list =[23,45,46,33,55,66,89,88,99,110,22,44,22]
for a in list:
    if a>110:
        break
    if a%11==0:
        print(a)
