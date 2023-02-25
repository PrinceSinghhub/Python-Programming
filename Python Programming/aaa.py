a=[1,2,3]
b=[1,2,3,4,5]
c=[1,2,3,4]
d=[]
for i in range(len(a)):
    d.append(a[i]+b[i]+c[i])
for j in range(len(a),len(c)):
    d.append(b[j]+c[j])
for k in range(len(c),len(b)):
    d.append(b[k])
print(d)
