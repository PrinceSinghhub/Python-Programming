n1 = int(input("n1"))
n2 = int(input("n2"))
max = 0
if n1 > n2:
    max = n1
elif n2 > n1:
    max = n2
p = max
lcm = 0
for i in range(max):
    if (p % n1 == 0 and p % n2 == 0):
        lcm = p
        break
    p += max
print(lcm)
